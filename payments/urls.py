# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from . import views

app_name = 'payments'
urlpatterns = [
    # url(r'^$', views.Payments.as_view(), name="payments"),
    url(r'^checkout/', views.Checkout.as_view(), name='checkout'),
    url(r'^confirmation/', views.Checkout.confirmation, name='checkout-confirmation'),

]