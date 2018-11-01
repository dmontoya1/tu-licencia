from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'webclient'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('reset-password/', views.PasswordResetView.as_view(), name='reset_password'),

]