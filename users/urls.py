from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'webclient'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('reset-password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('profile/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('change-email/', views.UserChangeEmail.as_view(), name='change_email'),
	path('change-password/', views.UserChangePassword.as_view(), name='change_password'),

]