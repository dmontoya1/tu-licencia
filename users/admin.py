# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as django_user_admin
from django.contrib.auth.forms import UserChangeForm as django_change_form
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
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
    exclude = ('deleted_at',)
    # actions = None
    extra_list_display = ('username', 'document_id','first_name', 'last_name', 'user_type')

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
    
    def get_list_display(self, request):
        """Modifica el 'list_display' predeterminado para mostrar siempre el estado de inhabilitación
        del objeto y los campos específicos de cada ModelAdmin, los cuales se agregan en 'extra_list_display'
        """
        if request.user.is_superuser:
            return self.extra_list_display + ('is_alive', )
        return self.list_display
        

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django.
        """
        query = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return query.all().exclude(is_superuser=True)
        else:
            return query.filter(pk=request.user.pk)
    
    def response_change(self, request, obj):
        """Modifica la respuesta de las acciones en el template de edición de objeto para 
        procesar el botón de 'Inhabilitar'.
        """

        opts = self.model._meta
        custom_redirect = False

        if "_soft-delete" in request.POST:
            obj.soft_delete() 
            custom_redirect = True

        if "_revive" in request.POST:
            obj.revive() 
            custom_redirect = True

        if custom_redirect:
            redirect_url = reverse('admin:%s_%s_changelist' % (opts.app_label, opts.model_name))
            return HttpResponseRedirect(redirect_url)
        else:
             return super(UserAdmin, self).response_change(request, obj)

    def is_alive(self, obj):
        """Método para evaluar si un objeto está inhabilitado o no y mostrar un 'check' en el 
        listado de objetos del admin.
        """

        icon = 'yes'
        if obj.deleted_at:
            icon = 'no'        
        return format_html(
            '<img src="/static/admin/img/icon-{icon}.svg" alt="{icon}">'.format(
                icon=icon
            )
        )
    is_alive.short_description = '¿Habilitado?'


admin.site.register(User, UserAdmin)