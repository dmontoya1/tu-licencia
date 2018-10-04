# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as django_user_admin
from django.contrib.auth.forms import UserChangeForm as django_change_form
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import User


class UserChangeForm(django_change_form):
    class Meta(django_change_form.Meta):
        model = User


class UserAdmin(django_user_admin):
    """Administrador de Usuarios
    """

    form = UserChangeForm
    model = User
    search_fields = (
        'first_name', 'last_name', 'email', 'cellphone', 'document_id'
    )
    list_display = (
        'username', 'document_id','first_name', 'last_name', 'user_type'
    )

    # fieldsets = (
    #     (None,
    #      {'fields':
    #       ('username', 'password')}),
    #     (_('Información Personal'), {'fields': ('first_name', 'last_name', 'email', 'user_type', 'document_type',
    #                                             'document_id', 'gender', 'birth_date')}),
    #     (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                  'groups')}),
    #     (_('Información Adicional'),
    #      {'fields': ('phone_number', 'cellphone', 'state', 'city', 'address',)})
    # )
    manager_fieldsets = (
        (None,
         {'fields':
          ('username', 'password')}),
        (_('Información Personal'), {'fields': ('first_name', 'last_name', 'email', 'document_type',
                                                'document_id', 'gender', 'birth_date')}),
        (_('Información Adicional'),
         {'fields': ('phone_number', 'cellphone', 'state', 'city', 'address',)})
    )

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )

    def get_fieldsets(self, request, obj=None):
        """
        Hook for specifying fieldsets.
        """
        if request.user.is_superuser:
            return [(None, {'fields': self.get_fields(request, obj)})]
            # return self.fieldsets
        else:
            return self.manager_fieldsets
    

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django.
        """
        query = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return query.all().exclude(is_superuser=True)
        else:
            return query.filter(pk=request.user.pk)


admin.site.register(User, UserAdmin)