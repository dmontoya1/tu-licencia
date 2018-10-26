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


from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence
from manager.models import State, City
from request.models import Request, RequestTramit
from users.models import User


class Checkout(TemplateView):
    """Vista para ver el formulario de seleccionar plan y moneda
    que se va a comprar
    """

    @csrf_exempt
    def post(self, request):
        print (request.body)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        p_tax = 0
        p_description = "Compra realizada desde TuLicencia"

        if settings.DEBUG:
            p_test_request = True
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
            host = 'http://tulicencia.apptitud.com.co'
        else:
            p_test_request = False
            p_cust_id_cliente='24075'
            p_key='ed2f55246c2728e27fd7ba67ee4c22e9a7984fc6'
            host = 'http://tulicencia.co'

        try:
            user_data = body['user']
            cea = Cea.objects.get(pk=body['cea'])
            crc = Crc.objects.get(pk=body['crc'])
            transit = TransitDepartment.objects.get(pk=body['transit'])
            crc_price = body['crc_price']
            cea_price = body['cea_price']
            transit_price = body['transit_price']
            tramits = body['tramits']

            city = City.objects.get(pk=user_data['city'])
            state = city.state
            try:
                user = User.objects.get(username=user_data['document_id'])
            except User.DoesNotExist:
                birth_date = datetime.strptime(user_data['birth_date'], '%m-%d-%Y')
                user = get_user_model()
                user = user()
                user.username = user_data['document_id']
                user.email = user_data['email']
                user.set_password(user_data['password'])
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.cellphone = user_data['cellphone']
                user.user_type = User.CLIENTE
                user.document_type = user_data['document_type']
                user.document_id = user_data['document_id']
                user.state = state
                user.city = city
                user.gender = user_data['gender']
                user.birth_date = birth_date
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                Token.objects.create(user=user)

            if (body['runt'] == 'si'):
                runt = True
            else:
                runt = False
            
            total_price = int(crc_price) + int(cea_price) + int(transit_price)

            request_obj = Request(
                user=user,
                cea=cea,
                crc=crc,
                transit=transit,
                payment_type = body['payment_type'],
                has_runt=runt,
                total_price=total_price
            )
            request_obj.save()
            
            licence1 = tramits['licence_1']
            licence2 = tramits['licence_2']

            tramit1 = RequestTramit(
                request=request_obj,
                tramit_type=licence1['tramit'],
                licence=Licence.objects.get(category=licence1['licence'])
            )
            tramit1.save()
            if (licence2 != ''):
                tramit2 = RequestTramit(
                    request=request_obj,
                    tramit_type=licence2['tramit'],
                    licence=Licence.objects.get(category=licence2['licence'])
                )
                tramit2.save()
        except Exception as e:
            print ("Expeption")
            print (e)

        p_currency_code = 'COP'
        p_amount = total_price
        p_amount_base = 0
        p_id_invoice = 'SO_{}_{}_{}'.format(request_obj.user.pk, request_obj.pk, int(time.mktime(datetime.now().timetuple())))
        p_url_response = '{}/payments/confirmation/'.format(host)
        p_url_confirmation = '{}/payments/confirmation/'.format(host)
        p_confirm_method = 'POST'
        p_signature = '{}^{}^{}^{}^{}'.format(p_cust_id_cliente, p_key, p_id_invoice, p_amount, p_currency_code)
        p_signature = hashlib.md5(p_signature.encode('utf-8')).hexdigest()

        ctx = {
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
        }

        return render(
            request,
            'payments/checkout.html',
            ctx
        )

# class Checkout(TemplateView):
#     """
#     """

#     template_name = 'payments/checkout.html'

    @csrf_exempt
    def confirmation(self, request):
        if settings.DEBUG:
            apiKey = '4Vj8eK4rloUd272L48hsrarnUA'
        else:
            apiKey = 'IXltfYxCYPA2efIuyqj3L8k3uG'
        
        if request.method == "POST":
            print ("POST")
            merchand_id = request.POST['merchant_id']
            reference_sale = request.POST['reference_sale']
            reference_pol = request.POST['reference_pol']
            state_pol = request.POST['state_pol']
            value  = request.POST['value']
            currency = request.POST['currency']
            sign = request.POST['sign']
            date = request.POST['date']

            value_str = str(value)

            value_antes, value_despues = value_str.split(".")
            value_despues = list(value_despues)
            if value_despues[1] == '0':
                value= round(float(value),1)
            signature = '{}~{}~{}~{}~{}~{}'.format(apiKey, merchand_id,reference_sale, value, currency,state_pol)
            signature = hashlib.md5(signature).hexdigest()

            user = reference_sale.split('_')

            if signature == sign:
                user = Staff.objects.filter(pk=user[1])
                invoice = Invoice.objects.filter(user=user, is_discharged=False).last()

                #Aprobada
                if state_pol == '4':
                    invoice.payment_date = datetime.now()
                    invoice.payu_reference_code = reference_pol
                    invoice.payment_status = Invoice.APPROVED
                    invoice.is_discharged = True
                    invoice.save()
                    return HttpResponse(status=200)
                #Declinada
                elif state_pol == '6':
                    invoice.payment_date = datetime.now()
                    invoice.payu_reference_code = reference_pol
                    invoice.payment_status = Invoice.REJECTED
                    invoice.is_discharged = False
                    invoice.save()
                    return HttpResponse(status=200)
                #Error
                elif state_pol == '104':
                    invoice.payment_date = datetime.now()
                    invoice.payu_reference_code = reference_pol
                    invoice.payment_status = Invoice.CANCEL
                    invoice.is_discharged = False
                    invoice.save()
                    return HttpResponse(status=200)
                #Expirada
                elif state_pol == '5':
                    invoice.payment_date = datetime.now()
                    invoice.payu_reference_code = reference_pol
                    invoice.payment_status = Invoice.CANCEL
                    invoice.is_discharged = False
                    invoice.save()
                    return HttpResponse(status=200)
                #Pendiente
                elif state_pol == '7':
                    invoice.payment_date = datetime.now()
                    invoice.payu_reference_code = reference_pol
                    invoice.payment_status = Invoice.PENDING
                    invoice.is_discharged = False
                    invoice.save()
                    return HttpResponse(status=200)
                #ninguno de los state_pol
                else:
                    return HttpResponse(status=500)
            else:
                return HttpResponse(status=500)
        
        elif request.method == "GET":
            merchand_id = request.GET.get('merchantId','')
            referenceCode = request.GET.get('referenceCode','')
            transactionState = request.GET.get('transactionState','')
            value = request.GET.get('TX_VALUE','')
            currency = request.GET.get('currency','')
            signature_get = request.GET.get('signature','')
            reference_pol = request.GET.get('reference_pol')
            polPaymentMethodType = request.GET.get('polPaymentMethodType')

            value_str = str(value)

            value_antes, value_despues = value_str.split(".")

            value_despues= list(value_despues)
            
            primer_parametro_despues = int(value_despues[0])
            segundo_parametro_despues = int(value_despues[1])

            if primer_parametro_despues % 2 == 0:
                if segundo_parametro_despues == 5:
                    value_1= value-0.1
                    value = round(value_1,1)
                else:
                    value = round(float(value),1)
            elif primer_parametro_despues % 2 != 0: 
                if segundo_parametro_despues == 5:
                    value_1= value+0.1
                    value = round(float(value_1),1)
                else:
                    value = round(float(value),1)
            
            signature = '{}~{}~{}~{}~{}~{}'.format(apiKey, merchand_id,referenceCode, value, currency,transactionState)
            signature = hashlib.md5(signature).hexdigest()

           
            if signature == signature_get:  

                return render(
                    request,
                    'payments/payment-resumen.html',
                    {
                        'merchand_id':merchand_id, 
                        'referenceCode':referenceCode,
                        'transactionState':transactionState,
                        'value':value,
                        'currency':currency,
                        'id_compra':referenceCode,
                        'reference_pol': reference_pol,
                        'polPaymentMethodType': polPaymentMethodType,
                    }
                    
                ) 
        else:
            return HttpResponseNotAllowed("Método no permitido")

