from django import forms
from .models import Event, Molinete, Credential

class RegisterEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'code']


class RegisterMolineteForm(forms.ModelForm):

    class Meta:
        model = Molinete
        fields = ['identity', 'event']


class RegisterCredentialForm(forms.ModelForm):

    class Meta:
        model = Credential
        fields = ['identity', 'molinete']



class ReadCredentialForm(forms.ModelForm):

    class Meta:
        model = Credential
        fields = ['identity', 'molinete']

