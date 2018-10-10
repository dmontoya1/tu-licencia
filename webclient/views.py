
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from companies.models import TuLicencia
from request.models import Request

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


class BaucherView(TemplateView):
    """Clase para ver el template del Boucher
    """

    template_name = 'webclient/baucher.html'

    def get_context_data(self, **kwargs):
        context = super(BaucherView, self).get_context_data(**kwargs)
        request = Request.objects.get(pk=self.kwargs['pk'])
        tulicencia = TuLicencia.objects.filter(city=request.user.city).first()
        context['request'] = request
        context['tulicencia'] = tulicencia
        return context
