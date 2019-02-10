from django.core.exceptions import ValidationError
from django.db import models

class Event(models.Model):
    """
    This class defines events in our app.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    code = models.CharField(max_length=50, default='')

    @property
    def credentialsRead(self):
        """
        Returns all the credentials read for a particular event.
        """
        count = 0
        for molinete in self.molinete_set.all():
            count += molinete.credential_set.filter(read=True).count()
        return count


    class Meta:
        ordering = ('created',)


    def __str__(self):
        return self.title


class Molinete(models.Model):
    """
    Defines the molinete(turnstile) which pertains to an event and can
    read credentials.
    """
    created = models.DateTimeField(auto_now_add=True)
    identity = models.CharField(max_length=100, blank=True, default='')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def read(self, credential):
        """
        Reads a credential and sets is read status to True.
        """
        credential.save()

    @property
    def credentialsRead(self):
        """
        Returns the credentials read by one particular Molinete.
        """
        return self.credential_set.filter(read=True).count()


    def __str__(self):
        return self.identity + ' | ' + self.event.title

class Credential(models.Model):
    """
    Allows to create credentials which pertain to a molinete in an event.
    """
    created = models.DateTimeField(auto_now_add=True)
    identity = models.CharField(max_length=100, blank=True, default='')
    molinete = models.ForeignKey(Molinete, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        is_adding = self._state.adding # check if we are updating or adding a new credential
        super().save(*args, **kwargs) # call the origin save method

        if not is_adding:
            self.read = True
            super().save(*args, **kwargs) # call the origin save method

    def __str__(self):
        return self.identity + ' | ' + self.molinete.identity + ' | ' + self.molinete.event.title

