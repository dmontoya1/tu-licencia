# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Avg, Count, Min, Sum, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from jet.dashboard.modules import DashboardModule

from companies.models import Cea, Crc, TransitDepartment
from manager.models import State, City
from request.models import Request, RequestTramit
from request.serializers import RequestSerializer



class ReportView(TemplateView):
    template_name = 'reports/reports.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ReportView, self).get_context_data(**kwargs)
    #     context['stores'] = Store.objects.all()
    #     states = State.objects.all()
    #     context['states'] = State.objects.all()
    #     return context
    
    # def generate_pdf_report(self, request, report, start_date, end_date):
    #     if report == "register_products":
    #         products = Product.objects.filter(date_added__gte=start_date, date_added__lte=end_date)
    #         context = {
    #             'headers': (
    #                 'Nombre',
    #                 'Descripción',
    #                 'Precio',
    #             ),
    #             'products': products,
    #             'start_date': start_date,
    #             'end_date': end_date
    #         }
    #         report_template_name = 'reports/products_registered.html'
    #     elif report == "number_services":
    #         store = Store.objects.get(pk=request.POST['store'])
    #         orders = Order.objects.filter(
    #             related_items__product__store=store, 
    #             status='DE', 
    #             date_added__gte=start_date, 
    #             date_added__lte=end_date
    #         )
    #         orders_count = orders.count()
    #         total_no_tax = 0
    #         total_tax = 0
    #         total_with_tax = 0
    #         if orders_count > 0:
    #             for order in orders:
    #                 total_no_tax += order.get_total_no_tax()
    #                 total_tax += order.get_total_tax()
    #                 total_with_tax += order.get_total_with_tax()

    #         context = {
    #             'store': store,
    #             'count': orders_count,
    #             'start_date': start_date,
    #             'end_date': end_date,
    #             'total_no_tax': total_no_tax,
    #             'total_tax': total_tax,
    #             'total_with_tax': total_with_tax
    #         }
    #         report_template_name = 'reports/number_services.html'
    #     elif report == "rating":
    #         orders = Order.objects.filter(date_added__gte=start_date, date_added__lte=end_date)

    #         context = {
    #             'headers': (
    #                 'Establecimiento',
    #                 '# Orden', 
    #                 'Fecha', 
    #                 'Calificación',
    #                 'Nombre de usuario',
    #                 'Correo',
    #                 'Teléfono'
    #             ),
    #             'orders': orders
    #         }
    #         report_template_name = 'reports/ratings.html'
    #     elif report == "sales":
    #         city = City.objects.get(pk=request.POST['city'])
    #         store = Store.objects.get(pk=request.POST['store'])
    #         orders = Order.objects.filter(
    #             related_items__product__store=store,
    #             date_added__gte=start_date, 
    #             date_added__lte=end_date,
    #             status='DE'
    #         )
             
    #         context = {
    #             'headers': (
    #                 'Establecimiento',
    #                 '# Orden', 
    #                 'Fecha', 
    #                 'Estado',
    #                 'Precio total',
    #                 'Valor Domicilio'
    #             ),
    #             'orders': orders,
    #             'store': store,
    #             'start_date':start_date,
    #             'end_date': end_date
    #         }
    #         report_template_name = 'reports/sales.html'
    #     elif report == "requests":
    #         city = City.objects.get(pk=request.POST['city'])
    #         store = Store.objects.get(pk=request.POST['store'])
    #         orders = Order.objects.filter(
    #             related_items__product__store=store,
    #             date_added__gte=start_date, 
    #             date_added__lte=end_date,
    #         )

    #         context = {
    #             'headers': (
    #                 'Establecimiento',
    #                 '# Orden', 
    #                 'Fecha', 
    #                 'Estado',
    #                 'Precio total',
    #                 'Nombre usuario',
    #                 'Correo'
    #             ),
    #             'orders': orders,
    #             'store': store,
    #             'start_date':start_date,
    #             'end_date': end_date
    #         }
    #         report_template_name = 'reports/requests.html'
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    #     result = generate_pdf(report_template_name, file_object=response, context=context)
    #     return response
    
    # def post(self, request, *args, **kwargs):
    #     report = request.POST['report']
    #     start_date = request.POST['start']
    #     end_date = request.POST['end']
    #     return self.generate_pdf_report(request, report, start_date, end_date)


class Purchases(TemplateView):
    """
    """

    template_name = 'reports/purchases.html'

    def get_context_data(self, **kwargs):
        context = super(Purchases, self).get_context_data(**kwargs)
        context['states'] = State.objects.alive().order_by('name')
        return context


class PurchaseApi(APIView):

    def post(self, request, format=None):
        try:
            start_date = request.data['start']
            end_date = request.data['end']
            city = request.data['city']

            requests = Request.objects.filter(
                request_date__gte=start_date,
                request_date__lte=end_date,
                crc__city=city
            )

            if(request.data['tramit']):
                requests = requests.filter(related_tramits__tramit_type=request.data['tramit'])
            
            serializer = RequestSerializer(requests, many=True)
            return Response(serializer.data)

        except Exception as e:
            print (e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class Credits(TemplateView):
    """
    """

    template_name = 'reports/credits.html'

    def get_context_data(self, **kwargs):
        context = super(Credits, self).get_context_data(**kwargs)
        context['states'] = State.objects.alive().order_by('name')
        return context


class CreditsApi(APIView):

    def post(self, request, format=None):
        try:
            start_date = request.data['start']
            end_date = request.data['end']
            city = request.data['city']

            requests = Request.objects.filter(
                request_date__gte=start_date,
                request_date__lte=end_date,
                crc__city=city,
                payment_type=Request.CREDITO
            )

            if(request.data['tramit']):
                requests = requests.filter(related_tramits__tramit_type=request.data['tramit'])
            
            if(request.data['credit_status']):
                requests = requests.filter(credit_status=request.data['credit_status'])
            
            serializer = RequestSerializer(requests, many=True)
            return Response(serializer.data)

        except Exception as e:
            print (e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class ServicesByCompany(TemplateView):
    """
    """

    template_name = 'reports/services_companies.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesByCompany, self).get_context_data(**kwargs)
        context['states'] = State.objects.alive().order_by('name')
        return context


class ServicesByCompanyApi(APIView):

    def post(self, request, format=None):
        try:
            start_date = request.data['start']
            end_date = request.data['end']
            city = request.data['city']

            query = []

            requests = Request.objects.filter(
                request_date__gte=start_date,
                request_date__lte=end_date,
                crc__city=city,
            )

            if (request.data['request_status']):
                requests = requests.filter(request_status=request.data['request_status'])

            if(request.data['cea']):
                cea = Cea.objects.get(pk=request.data['cea'])
                requests = requests.filter(cea=cea)

                for r in requests:
                    if r.cea:
                        tramits = []
                        for t in r.related_tramits.all():
                            tramits.append(
                                {
                                    'tramit': t.name()
                                }
                            )
                        if r.payment_date:
                            payment_date = r.payment_date.strftime("%d %B, %y - %I:%M %p")
                        else:
                            payment_date = "Sin pago"
                        query.append(
                            {
                                'name': r.cea.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )
            
            elif(request.data['crc']):
                crc = Crc.objects.get(pk=request.data['crc'])
                requests = requests.filter(crc=crc)

                for r in requests:
                    if r.crc:
                        tramits = []
                        for t in r.related_tramits.all():
                            tramits.append(
                                {
                                    'tramit': t.name()
                                }
                            )
                        if r.payment_date:
                            payment_date = r.payment_date.strftime("%d %B, %y - %I:%M %p")
                        else:
                            payment_date = "Sin pago"
                        query.append(
                            {
                                'name': r.crc.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )

            elif(request.data['transit']):
                transit = TransitDepartment.objects.get(pk=request.data['transit'])
                requests = requests.filter(transit=transit)

                for r in requests:
                    if r.transit:
                        tramits = []
                        for t in r.related_tramits.all():
                            tramits.append(
                                {
                                    'tramit': t.name()
                                }
                            )
                        if r.payment_date:
                            payment_date = r.payment_date.strftime("%d %B, %y - %I:%M %p")
                        else:
                            payment_date = "Sin pago"
                        query.append(
                            {
                                'name': r.transit.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )
            else:

                for r in requests:
                    tramits = []
                    for t in r.related_tramits.all():
                        tramits.append(
                            {
                                'tramit': t.name()
                            }
                        )
                    if r.payment_date:
                        payment_date = r.payment_date.strftime("%d %B, %y - %I:%M %p")
                    else:
                        payment_date = "Sin pago"
                    if r.cea:
                        query.append(
                            {
                                'name': r.cea.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )
                    if r.crc:
                        query.append(
                            {
                                'name': r.crc.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )
                    if r.transit:
                        query.append(
                            {
                                'name': r.transit.name,
                                'client_name': r.user.get_full_name(),
                                'tramits': tramits,
                                'request_date': r.request_date.strftime("%d %B, %y - %I:%M %p"),
                                'payment_date': payment_date,
                                'request_status': r.get_request_status_display(),
                                'payment_type': r.get_payment_type_display(),
                                'booking': r.booking
                            }
                        )
            
            
            return JsonResponse(query, safe=False)

        except Exception as e:
            print (e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class CeaServices(TemplateView):
    """
    """

    template_name = 'reports/cea_services.html'


class CeaServicesApi(APIView):

    def post(self, request, format=None):
        try:
            start_date = request.data['start']
            end_date = request.data['end']
            cea = request.user.cea
            print (cea)

            requests = Request.objects.filter(
                cea=cea,
                request_date__gte=start_date,
                request_date__lte=end_date,
                request_status=Request.PAID
            )
            print (requests)

            if(request.data['cea_status']):
                requests = requests.filter(cea_status=request.data['cea_status'])
            
            serializer = RequestSerializer(requests, many=True)
            return Response(serializer.data)

        except Exception as e:
            print (e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class CrcServices(TemplateView):
    """
    """

    template_name = 'reports/crc_services.html'


class CrcServicesApi(APIView):

    def post(self, request, format=None):
        try:
            start_date = request.data['start']
            end_date = request.data['end']
            crc = request.user.crc

            requests = Request.objects.filter(
                crc=crc,
                request_date__gte=start_date,
                request_date__lte=end_date,
                request_status=Request.PAID
            )

            if(request.data['crc_status']):
                requests = requests.filter(crc_status=request.data['crc_status'])
            
            serializer = RequestSerializer(requests, many=True)
            return Response(serializer.data)

        except Exception as e:
            print (e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)
