from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'webclient'
urlpatterns = [
    path('', views.Stepper.as_view(), name='stepper'),
    path('crc-detail', views.CRCDetail.as_view(), name='crc-detail'),
    path('cea-detail', views.CEADetail.as_view(), name='cea-detail'),
    path('transit-detail', views.TransitDetail.as_view(), name='transit-detail'),
    path('baucher/<int:pk>/request', views.BaucherView.as_view(), name='baucher-detail'),
    path('contact-form', views.ContactForm.as_view(), name='contact-form'),
    path('login', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('forget-password/', views.ForgetPassword.as_view(), name='forget_password'),
    path('recover-password/', views.ResetPasswordView.as_view(), name='recover_password'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('request/<int:pk>/', views.RequestDetail.as_view(), name='request-detail'),
]