# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json
import time

from datetime import datetime

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, View, ListView

from core.views import sendEmail
from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence
from manager.models import State, City
from request.models import Request, RequestTramit
from users.models import User


class Checkout(TemplateView):
    """Vista para ver el formulario de seleccionar plan y moneda
    que se va a comprar
    """

    template_name = 'payments/checkout.html'

    @csrf_exempt
    def post(self, request):
        p_tax = 0
        p_description = "Compra realizada desde TuLicencia"
        p_split_type = '01'
        
        if settings.DEBUG:
            p_test_request = True
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
            p_split_merchant_receiver = '24075'
            p_split_primary_receiver = '24075'
            p_split_primary_receiver_fee = 0
            host = 'http://distulo.serveo.net/'
        else:
            p_test_request = False
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
            p_split_merchant_receiver = '24075'
            p_split_primary_receiver = '24075'
            p_split_primary_receiver_fee = 0
            host = 'http://3.16.156.133'

        try:
            try:
                cea = Cea.objects.get(pk=request.POST['cea'])
            except:
                cea = None
            crc = Crc.objects.get(pk=request.POST['crc'])
            transit = TransitDepartment.objects.get(pk=request.POST['transit'])
            crc_price = request.POST['crc_price']
            cea_price = request.POST['cea_price']
            transit_price = request.POST['transit_price']
            licence_1 = request.POST['licence_1']
            tramit_1 = request.POST['tramit_1']
            licence_2 = request.POST['licence_2']
            tramit_2 = request.POST['tramit_2']

            state = State.objects.get(pk=request.POST['state'])
            # state = city.state
            try:
                user = User.objects.get(username=request.POST['document_id'])
            except User.DoesNotExist:
                birth_date = datetime.strptime(request.POST['birth_date'], '%m/%d/%Y')
                user = get_user_model()
                user = user()
                user.username = request.POST['document_id']
                user.email = request.POST['email']
                user.set_password(request.POST['password1'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.cellphone = request.POST['phone_number']
                user.user_type = User.CLIENTE
                user.document_type = request.POST['doc_type']
                user.document_id = request.POST['document_id']
                user.state = state
                # user.city = city
                user.gender = request.POST['gender']
                user.birth_date = birth_date
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                Token.objects.create(user=user)

            if (request.POST['runt'] == 'si'):
                runt = True
            else:
                runt = False
            
            total_price = float(crc_price) + float(cea_price) + float(transit_price)
            p_split_primary_receiver_fee = (float(crc_price) * 0.2) + (float(cea_price) * 0.2) + float(transit_price)
            print (p_split_primary_receiver_fee)
            crc_price_final = float(crc_price) - (float(float(crc_price) * 0.2))
            print (crc_price_final)
            cea_price_final = float(cea_price) - (float(float(cea_price) * 0.2))
            print (cea_price_final)

            request_obj = Request(
                user=user,
                cea=cea,
                crc=crc,
                transit=transit,
                payment_type = 'CO',
                has_runt=runt,
                total_price=total_price,
                paper=request.POST['paper']
            )
            request_obj.save()

            tramit1 = RequestTramit(
                request=request_obj,
                tramit_type=tramit_1,
                licence=Licence.objects.get(category=licence_1)
            )
            tramit1.save()
            if (licence_2 != ''):
                tramit2 = RequestTramit(
                    request=request_obj,
                    tramit_type=tramit_2,
                    licence=Licence.objects.get(category=licence_2)
                )
                tramit2.save()
        except Exception as e:
            print ("Exception")
            print (e)

        p_currency_code = 'COP'
        p_amount = int(total_price)
        p_amount_base = 0
        p_signature_receivers = ''
        p_split_receivers = []
        p_id_invoice = 'SO_{}_{}_{}'.format(request_obj.user.pk, request_obj.pk, int(time.mktime(datetime.now().timetuple())))
        request_obj.id_invoice = p_id_invoice
        request_obj.save()
        p_url_response = '{}/payments/confirmation/'.format(host)
        p_url_confirmation = '{}/payments/confirmation/'.format(host)
        p_confirm_method = 'POST'
        p_signature = '{}^{}^{}^{}^{}'.format(p_cust_id_cliente, p_key, p_id_invoice, p_amount, p_currency_code)
        p_signature = hashlib.md5(p_signature.encode('utf-8')).hexdigest()
        p_split_receivers.append({'id': cea.epayco_code, 'fee': str(cea_price_final)})
        # p_split_receivers.append({'id': crc.epayco_code, 'fee': str(crc_price_final)})

        print (p_split_receivers)

        for r in p_split_receivers:
            p_signature_receivers += r['id'] + '^' + r['fee']

        p_signature_split = '{}^{}^{}^{}^{}'.format(p_split_type, p_split_merchant_receiver, p_split_primary_receiver,
                                             p_split_primary_receiver_fee, p_signature_receivers)
        p_signature_split = hashlib.md5(p_signature_split.encode('utf-8')).hexdigest()

        ctx = {
            'cea': cea,
            'crc': crc,
            'transit': transit,
            'crc_price': int(crc_price),
            'cea_price': int(cea_price),
            'transit_price': int(transit_price),
            'user': request_obj.user,
            'request_obj': request_obj,
            'p_description': p_description,
            'p_cust_id_cliente' : p_cust_id_cliente,
            'p_key' : p_key,
            'p_id_invoice': p_id_invoice,
            'p_amount' : p_amount,
            'p_tax' : p_tax,
            'p_amount_base' : p_amount_base,
            'p_email': request_obj.user.email,
            'p_currency_code' : p_currency_code,
            'p_signature' : p_signature,
            'p_test_request' : p_test_request,
            'p_url_response' : p_url_response,
            'p_url_confirmation' : p_url_confirmation,
            'p_confirm_method': p_confirm_method,
            'p_split_type': p_split_type,
            'p_split_merchant_receiver': p_split_merchant_receiver,
            'p_split_primary_receiver': p_split_primary_receiver,
            'p_split_primary_receiver_fee': p_split_primary_receiver_fee,
            'p_split_receivers': p_split_receivers,
            'p_signature_split': p_signature_split,

        }

        return render(
            request,
            'payments/checkout.html',
            ctx
        )

    @csrf_exempt
    def confirmation(self):
        print (self.method)
        if settings.DEBUG:
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
        else:
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
        
        if self.method == "POST":
            print ('POSTTTTTTT')
            print (self.POST)
            x_cust_id_cliente = self.POST['x_cust_id_cliente']
            x_id_invoice = self.POST['x_id_invoice']
            x_currency_code = self.POST['x_currency_code']
            x_franchise = self.POST['x_franchise']
            x_transaction_date = self.POST['x_transaction_date']
            x_amount  = self.POST['x_amount']
            x_transaction_id = self.POST['x_transaction_id']
            x_ref_payco = self.POST['x_ref_payco']
            x_signature = self.POST['x_signature']
            x_response = self.POST['x_response']
            x_cod_response = self.POST['x_cod_response']

            signature = '{}^{}^{}^{}^{}^{}'.format(p_cust_id_cliente, p_key, x_ref_payco, x_transaction_id, x_amount,x_currency_code)
            signature = hashlib.sha256(signature.encode('utf-8')).hexdigest()

            print (x_signature)
            print (signature)

            if signature == x_signature:
                print ("Signs iguales")
                request_obj = Request.objects.get(id_invoice=x_id_invoice)

                #Aceptada
                if x_cod_response == '1':
                    request_obj.payment_date = x_transaction_date
                    request_obj.payment_status = x_response
                    request_obj.request_status = Request.PAID
                    request_obj.id_epayco_invoice = x_ref_payco
                    request_obj.save()
                    ctx = {
                        'request':request
                    }
                    sendEmail(ctx, request_obj.user.email, 'Instrucciones TuLicencia', 'webclient/baucher.html')
                    return HttpResponse(status=200)
                #Rechazada
                elif x_cod_response == '2':
                    request_obj.payment_date = x_transaction_date
                    request_obj.payment_status = x_response
                    request_obj.id_epayco_invoice = x_ref_payco
                    request_obj.save()
                    return HttpResponse(status=200)
                #Pendiente
                elif x_cod_response == '3':
                    request_obj.payment_date = x_transaction_date
                    request_obj.payment_status = x_response
                    request_obj.id_epayco_invoice = x_ref_payco
                    request_obj.save()
                    return HttpResponse(status=200)
                #Fallida
                elif x_cod_response == '4':
                    request_obj.payment_date = x_transaction_date
                    request_obj.payment_status = x_response
                    request_obj.id_epayco_invoice = x_ref_payco
                    request_obj.save()
                    return HttpResponse(status=200)
                #ninguno de los state_pol
                else:
                    return HttpResponse(status=500)
            else:
                print ("Sign diferentes")
                return HttpResponse(status=500)
        
        elif self.method == "GET":
            print (self.GET)
            x_cust_id_cliente = self.GET['x_cust_id_cliente']
            x_id_invoice = self.GET['x_id_invoice']
            x_description = self.GET['x_description']
            x_currency_code = self.GET['x_currency_code']
            x_franchise = self.GET['x_franchise']
            x_transaction_date = self.GET['x_transaction_date']
            x_amount  = self.GET['x_amount']
            x_transaction_id = self.GET['x_transaction_id']
            x_ref_payco = self.GET['x_ref_payco']
            x_signature = self.GET['x_signature']
            x_response = self.GET['x_response']
            x_cod_response = self.GET['x_cod_response']

            request_obj = Request.objects.get(id_invoice=x_id_invoice)

            return render(
                self,
                'payments/payment-resumen.html',
                {
                    'fullname':request_obj.user.get_full_name(), 
                    'x_description':x_description,
                    'x_amount':x_amount,
                    'x_transaction_date': x_transaction_date,
                    'x_id_invoice': x_id_invoice
                }
                
            ) 
        else:
            return HttpResponseNotAllowed("Método no permitido")

