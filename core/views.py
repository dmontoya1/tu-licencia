# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template

from .render_to_file import Render

def sendEmail(ctx=None, email_to=None, subject=None, template='emails/email.html'):
	"""Función para enviar mensajes en la plataforma
	
	Esta función se utiliza para enviar mensajes en la plataforma, recibe como parámetros
	un contexto, el email hacia quien va dirigido, Asunto y el template base
	del correo
	"""

	if ctx != None and email_to != None:
		body = get_template(template).render(ctx)
		message = EmailMessage(subject, body, settings.EMAIL_USER, [email_to])
		message.content_subtype = 'html'
		message.send()


def sendBaucherEmail(ctx=None, email_to=None, subject=None, template='emails/email.html', params=None):
	"""Función para enviar mensajes en la plataforma
	
	Esta función se utiliza para enviar mensajes en la plataforma, recibe como parámetros
	un contexto, el email hacia quien va dirigido, Asunto y el template base
	del correo
	"""

	if ctx != None and email_to != None:
		body = get_template(template).render(ctx)
		message = EmailMessage(subject, body, settings.EMAIL_USER, [email_to])
		pdf_name, pdf_file = Render.render_to_file('webclient/baucher.html', params)
		message.content_subtype = 'html'
		message.attach("instrucciones.pdf", pdf_file, "application/pdf")
		message.send()




