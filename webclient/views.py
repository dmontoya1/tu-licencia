
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

class Stepper(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/stepper.html'


class CRCDetail(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/crc_detail.html'


class CEADetail(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/cea_detail.html'


class TransitDetail(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/transit_detail.html'
