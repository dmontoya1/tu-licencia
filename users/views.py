# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, View, ListView

from api.helpers import CsrfExemptSessionAuthentication
from core.views import sendEmail
from .models import UserToken
from .serializers import UserSerializer, UserCustomSerializer, UserEmailSerializer, ChangePasswordSerializer


class Login(View):
    """Iniciar Sesión desde Cliente
    """

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            url = reverse('webclient:profile')
            login(request, user)
        else:
            response = {'error': 'El número de documento no se encuentra registrado / Contraseña incorrecta.'}
            return JsonResponse(response, status=400)

        return JsonResponse(url, safe=False)


class PasswordResetView(APIView):
	"""Api para olvidó su contraseña de un usuario
	"""

	serializer_class = UserCustomSerializer
	permission_classes = (AllowAny,)
	queryset = UserToken.objects.all()

	def get_object(self):
		document_id = self.request.data.get('document_id')
		try:
			user = get_user_model().objects.filter(document_id=document_id, user_type=get_user_model().CLIENTE).first()
		except get_user_model().DoesNotExist:
			raise  Http404("El usuario con este documento no existe en la base de datos")
		if user:
			try:
				obj = UserToken.objects.get(user=user)
			except:
				obj = UserToken.objects.create(user=user)
			return obj
		raise  Http404("El usuario con este documento no existe en la base de datos")


	def post(self, request, *args, **kwargs):
		user = self.get_object()
		token = uuid.uuid1().hex
		user.password_activation_token = token
		user.is_use_token = False
		user.save()
		url = 'http://{}{}?token={}'.format(request.get_host(), reverse('webclient:recover_password'), token)
		ctx = {
			"title": "Recuperar contraseña en TuLicencia",
			"content": "Hola! Solicitaste recuperar tu contraseña en TuLicencia. Para cambiarla has click en el siguiente botón",
			"url": url,
			"action": "Recuperar"
		}
		sendEmail(ctx, user.user.email, 'TuLicencia Cambio de contraseña')
		return Response(
			{
				"detail":"Se ha enviado un correo para restablecer su contraseña"
			},
			status=status.HTTP_200_OK
		)


class ProfileUpdate(generics.RetrieveUpdateAPIView):
	"""Api para actualizar los datos del perfil de usuario
	"""

	serializer_class = UserSerializer
	model = get_user_model()
	queryset = get_user_model().objects.all()

	def get_object(self):
		return self.request.user


class UserChangeEmail(generics.UpdateAPIView):
	"""Api para actualizar el email de un usuario
	"""

	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
	serializer_class = UserEmailSerializer
	queryset = get_user_model().objects.all()


	def get_object(self):
		pk = self.request.data.get('pk')
		try:
			obj = get_user_model().objects.get(pk=pk)
		except:
			raise ValidationError('El usuario no se encuentra registrado')
		return obj


class UserChangePassword(generics.UpdateAPIView):
	"""Api para actualizar el email de un usuario
	"""

	authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
	serializer_class = ChangePasswordSerializer
	queryset = get_user_model().objects.all()


	def get_object(self):
		return self.request.user
