import factory
import factory.django
from eventos.models import Event, Molinete, Credential

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = factory.Faker('title')
    code = factory.Faker('code')


class MolineteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Molinete

    identity = factory.Faker('identity')


class CredentialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Credential

    identity = factory.Faker('ean13')
