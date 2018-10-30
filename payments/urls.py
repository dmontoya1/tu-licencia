# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from . import views

app_name = 'payments'
urlpatterns = [
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('confirmation/', views.Checkout.confirmation, name='checkout-confirmation'),

]