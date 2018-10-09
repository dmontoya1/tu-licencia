from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView

from .models import Request
from .serializers import RequestSerializer


class RequestCreate(APIView):
    """
    """

    def post(self, request, *args, **kwargs):
        print (request.POST)
        print (request.data)
        # print (request.data)

        


