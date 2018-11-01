# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
from django.template import loader

from django.conf import settings


def sendEmail(ctx=None, email_to=None, subject=None, template='emails/email.html'):
	"""Función para enviar mensajes en la plataforma
	
	Esta función se utiliza para enviar mensajes en la plataforma, recibe como parámetros
	un contexto, el email hacia quien va dirigido, Asunto y el template base
	del correo
	"""

	if ctx != None and email_to != None:
		body = loader.get_template(template).render(ctx)
		message = EmailMessage(subject, body, settings.EMAIL_USER, [email_to])
		print (message)
		message.content_subtype = 'html'
		message.send()
		print ("Mensaje enviado")
