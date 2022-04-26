import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from applications.entrada.models import Entry
from .models import Home
from .forms import SuscriberForm, ContactForm

from django.views.generic import (
    TemplateView,
    CreateView
)

class TestPlantilla(TemplateView):
    template_name = "plantillas/register.html"

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        #Cargar el home
        context["home"] = Home.objects.latest("created")
        #Contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #Contexto para articulos en home
        context["entradas_home"] = Entry.objects.entradas_en__home()
        #Contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #Envio de formulario de suscripcion
        context["form"] = SuscriberForm
        return context

class SuscriberCreateView(CreateView):
    form_class = SuscriberForm
    success_url = '/'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '/'