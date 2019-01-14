# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView

from companies.models import TuLicencia
from manager.models import Police
from request.models import Request
from users.models import UserToken

class Stepper(TemplateView):
    """Vista para el stepper
    """

    template_name = 'webclient/stepper.html'


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
        requests = Request.objects.filter(user=self.request.user).order_by('request_date')
        context['requests'] = requests
        return context


class RequestDetail(LoginRequiredMixin, DetailView):
    """Detalle de una solicitud
    """

    model = Request
    template_name='webclient/request_detail.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'


class ProfileDetail(LoginRequiredMixin, DetailView):
    """Detalle de mi perfil
    """

    model = get_user_model()
    template_name='webclient/edit_profile.html'
    login_url = '/login'
    redirect_field_name = 'redirect_to'


class ForgetPassword(TemplateView):
    """Vista del olvidó la contraseña
    """

    template_name = 'webclient/forget_password.html'


class ResetPasswordView(TemplateView):
    """Vista para Recuperar la constraseña
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
                    "!Felicitaciones!, tu contraseña se ha cambiado correctamente, ahora puedes ingresar con tu nueva contraseña"
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
                return HttpResponseRedirect(reverse('web_client:forget_password'))

            context = self.get_context_data(user.user)
            return self.render_to_response(context)

        except MultiValueDictKeyError as e:
            print (e)
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