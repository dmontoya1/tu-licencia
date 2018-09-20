from django.shortcuts import render

from rest_framework import generics

from .models import Request
from .serializers import RequestSerializer


class RequestCreate(generics.ListCreateAPIView):
    """
    """

    serializer_class = RequestSerializer
    queryset = Request.objects.all()

