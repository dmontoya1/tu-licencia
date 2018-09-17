
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

class Stepper(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/stepper.html'
