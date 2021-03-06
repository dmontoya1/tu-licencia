# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from easy_pdf.views import PDFTemplateView

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView

from django_xhtml2pdf.utils import generate_pdf

from companies.models import TuLicencia, TransitDepartment, CeaRating, CrcRating, TransitRating
from manager.models import Police, State, City
from request.models import Request
from users.models import UserToken


class Stepper(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/stepper.html'


class BaucherView(PDFTemplateView):

    template_name = 'webclient/baucher.html'

    def get_context_data(self, **kwargs):
        request = Request.objects.get(pk=self.kwargs['pk'])
        tulicencia = TuLicencia.objects.filter(city=request.user.city).first()
        return super(BaucherView, self).get_context_data(
            pagesize='Letter',
            title='Baucher TuLicencia',
            request=request,
            tulicencia=tulicencia,
            **kwargs
        )


class ContactForm(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/contact_form.html'


class Login(TemplateView):
    """Vista para el login
    """

    template_name = 'webclient/login.html'


class Profile(LoginRequiredMixin, TemplateView):
    """Vista para el perfil
    """

    template_name = 'webclient/profile.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        if self.request.user.user_type == 'EXU':
            requests = Request.objects.filter(user_request=self.request.user).order_by('request_date')
        else:
            requests = Request.objects.filter(user=self.request.user).order_by('request_date')
        context['requests'] = requests
        return context


class RequestDetail(LoginRequiredMixin, DetailView):
    """Detalle de una solicitud
    """

    model = Request
    template_name = 'webclient/request_detail.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        print(self.request.user)
        context = super(RequestDetail, self).get_context_data(**kwargs)
        request_obj = Request.objects.get(pk=self.kwargs['pk'])
        user = request_obj.user
        cea_rt = False
        crc_rt = False
        transit_rt = False
        cea_rating = CeaRating.objects.filter(cea=request_obj.cea, user=user)
        crc_rating = CrcRating.objects.filter(crc=request_obj.crc, user=user)
        transit_rating = TransitRating.objects.filter(transit=request_obj.transit, user=user)
        if cea_rating.count() > 0:
            cea_rt = True
        if crc_rating.count() > 0:
            crc_rt = True
        if transit_rating.count() > 0:
            transit_rt = True
        context['cea_rating'] = cea_rt
        context['crc_rating'] = crc_rt
        context['transit_rating'] = transit_rt
        if self.request.user.user_type == 'EXU':
            context['express_user'] = self.request.user
        return context


class ProfileDetail(LoginRequiredMixin, DetailView):
    """Detalle de mi perfil
    """

    model = get_user_model()
    template_name='webclient/edit_profile.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'


class ForgetPassword(TemplateView):
    """Vista del olvid?? la contrase??a
    """

    template_name = 'webclient/forget_password.html'


class ResetPasswordView(TemplateView):
    """Vista para Recuperar la constrase??a
    """

    template_name = 'webclient/recover_password.html'

    def post(self, request, *args, **kwargs):
        try:
            document_id = request.POST.get('document_id')
            password = request.POST.get('password')
            user = get_user_model().objects.filter(document_id=document_id).first()
            user.set_password(password)
            user.save()
            user_token = UserToken.objects.get(user=user)
            user_token.is_use_token = True
            user_token.save()

            messages.add_message(
                request,
                    messages.SUCCESS, 
                    "!Felicitaciones!, tu contrase??a se ha cambiado correctamente, ahora puedes ingresar con tu nueva contrase??a"
            )
            return HttpResponseRedirect(reverse('webclient:login'))

        except MultiValueDictKeyError:
            return HttpResponseRedirect(reverse('webclient:login'))		

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            try:
                user = UserToken.objects.get(is_use_token=False, password_activation_token=token)
            except UserToken.DoesNotExist:
                messages.add_message(
                    request,
                        messages.ERROR, 
                        "Lo sentimos el enlace al que intenta acceder ha dejado de funcionar"
                )
                return HttpResponseRedirect(reverse('webclient:forget_password'))

            context = self.get_context_data(user.user)
            return self.render_to_response(context)

        except MultiValueDictKeyError as e:
            print(e)
            return HttpResponseRedirect(reverse('webclient:login'))

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self,user=None, **kwargs):
        context = super(ResetPasswordView, self).get_context_data(**kwargs)
        context['user'] = user
        return context


class TermsView(TemplateView):
    template_name = 'webclient/policy_detail.html'

    def get_context_data(self, **kwargs):
        police = get_object_or_404(Police, police_type='TC')
        context = super(TermsView, self).get_context_data(**kwargs)
        context['name'] = police.get_police_type_display()
        context['content'] = police.text
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'webclient/policy_detail.html'

    def get_context_data(self, **kwargs):
        police = get_object_or_404(Police, police_type='PP')
        context = super(PrivacyPolicyView, self).get_context_data(**kwargs)
        context['name'] = police.get_police_type_display()
        context['content'] = police.text
        return context


class TransitList(TemplateView):
    """ Vista para ver los departamentos de tr??nsito cuando se da click
    al flujo de duplicado
    """

    template_name = 'webclient/TransitList.html'

    def get_context_data(self, **kwargs):
        state = State.objects.get(pk=self.kwargs['state'])
        cities = City.objects.alive().filter(state=state).order_by('name')
        transits = TransitDepartment.objects.filter(state=state)
        context = super(TransitList, self).get_context_data(**kwargs)
        context['transits'] = transits
        context['cities'] = cities
        context['state'] = state
        return context
