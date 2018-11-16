# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView, View, ListView


from core.views import sendEmail
from .models import UserToken
from .serializers import UserSerializer, UserCustomSerializer


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
            response = {'error': 'Correo y/o contraseña incorrectas.'}
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
