# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from io import BytesIO

import os
import xhtml2pdf.pisa as pisa

from random import randint

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template

from django.conf import settings


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        file = open("instrucciones.pdf", "wb")
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), file)
        file.close()
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def render_to_file(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        file_name = "instrucciones.pdf"
        file_path = os.path.join(os.path.abspath(os.path.dirname("__file__")), "tulicencia", file_name)
        print (file_path)
        with open(file_path, 'wb') as pdf:
            print (pdf)
            pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
            print ("Salio del pisa")
        return [file_name, file_path]
