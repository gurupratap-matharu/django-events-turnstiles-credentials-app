import time
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import generic, View

from eventos.forms import RegisterEventForm, RegisterMolineteForm,RegisterCredentialForm,ReadCredentialForm
from eventos.models import Event, Molinete, Credential

class EventIndexView(generic.ListView):
    """
    CBV for generating simple index view of our event app.
    User can either chose to
    1. list all the events in the database
    2. Register a new event in the database
    """

    template_name = 'eventos/index.html'

    def get_queryset(self):
        return None

class EventRegisterView(View):
    """
    Our form class that uses class based views to render a register form.
    """
    form_class = RegisterEventForm
    template_name = 'eventos/form.html'

    def get(self, request, *args, **kwargs):
        """
        Our inbuilt GET method to render a new blank form
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        """
        Our inbuilt POST method to read a saved form or populate it with
        previously filled fields.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            code = form.cleaned_data['code']

            # create a event in our database
            Event.objects.create(title=title, code=code)

            # redirect to a the list all events url
            return HttpResponseRedirect(reverse('eventos:list'))

        return render(request, self.template_name, {'form': form})

class MolineteRegisterView(View):
    """
    Our form class that uses class based views to render a register form.
    """
    form_class = RegisterMolineteForm
    template_name = 'eventos/form.html'

    def get(self, request, *args, **kwargs):
        """
        Our inbuilt GET method to render a new blank form
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        """
        Our inbuilt POST method to read a saved form or populate it with
        previously filled fields.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            identity = form.cleaned_data['identity']
            event = form.cleaned_data['event']

            # create a event in our database
            Molinete.objects.create(identity=identity, event=event)

            # redirect to a the list all events url
            return HttpResponseRedirect(reverse('eventos:list'))

        return render(request, self.template_name, {'form': form})


class CredentialRegisterView(View):
    """
    Our form class that uses class based views to render a register form.
    """
    form_class = RegisterCredentialForm
    template_name = 'eventos/form.html'

    def get(self, request, *args, **kwargs):
        """
        Our inbuilt GET method to render a new blank form
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        """
        Our inbuilt POST method to read a saved form or populate it with
        previously filled fields.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            identity = form.cleaned_data['identity']
            molinete = form.cleaned_data['molinete']

            # create a event in our database
            Credential.objects.create(identity=identity, molinete=molinete)

            # redirect to a the list all events url
            return HttpResponseRedirect(reverse('eventos:list'))

        return render(request, self.template_name, {'form': form})


class CredentialReadView(View):
    """
    Our form class that uses class based views to render a register form.
    """
    form_class = ReadCredentialForm
    template_name = 'eventos/form.html'

    def get(self, request, *args, **kwargs):
        """
        Our inbuilt GET method to render a new blank form
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        """
        Our inbuilt POST method to read a saved form or populate it with
        previously filled fields.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            identity = form.cleaned_data['identity']
            molinete = form.cleaned_data['molinete']
            if Credential.objects.filter(identity=identity).exists():

                credential = Credential.objects.get(identity=identity)
                # check if molinete and credential are linked
                if molinete.credential_set.filter(identity=identity).exists():
                    molinete.read(credential)
                    # redirect to a the list all events url
                    # messages.success(request, 'Access Granted!')

                    # return HttpResponseRedirect()
                    return HttpResponseRedirect(reverse('eventos:list'))

            messages.error(request, 'Sorry. Credential not identified!!')
        return render(request, self.template_name, {'form': form})

class EventListView(generic.ListView):
    """
    Our List view class that used django's CBV and renders out a list of all the
    events in the database.
    """
    model = Event
    template_name = 'eventos/list.html'
    context_object_name = 'events'



class EventDetailView(generic.DetailView):
    """
    Our Detail view class that used django's CBV and shows the detail
    of any particular event in the database.
    """
    model = Event
    template_name = 'eventos/detail.html'
    context_object_name = 'event'


class MolineteDetailView(generic.DetailView):
    """
    Our Detail view class that used django's CBV and shows the detail
    of any particular molinete in the database.
    """
    model = Molinete
    template_name = 'eventos/molinete_detail.html'
    context_object_name = 'molinete'


