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
            print (start_date0)
            end_date = request.data['end']
            print (end_date)
            cea = request.user.cea
            print (cea)

            requests = Request.objects.filter(
                cea=cea,
                request_date__gte=start_date,
                request_date__lte=end_date,
                request_status=Request.PAID
            ).encode('utf-8')
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
