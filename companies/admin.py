# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin, messages

from users.models import User
from utils.admin import SoftDeletionModelAdminMixin
from .models import (
    Cea, Crc, TransitDepartment, Schedule, CeaLicence, CeaVehicle,
    TuLicencia, TransitLicence, CeaRating, CrcRating, TransitRating)


class ScheduleAdmin(admin.StackedInline):
    
    model = Schedule
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                'id', 'day', 'start_time', 'end_time', 'journey'
            ),
        }),
    )


class CeaLicenceAdmin(admin.StackedInline):
    """
    """

    model = CeaLicence
    extra = 1


class CeaVehicleAdmin(admin.StackedInline):
    """
    """
    model = CeaVehicle
    extra = 1


class TransitLicenceAdmin(admin.StackedInline):
    """
    """
    model = TransitLicence
    extra = 0


class CrcRatingAdmin(admin.StackedInline):
    """
    """
    model = CrcRating
    extra = 0


class CeaRatingAdmin(admin.StackedInline):
    """
    """
    model = CeaRating
    extra = 0


class TransitRatingAdmin(admin.StackedInline):
    """
    """
    model = TransitRating
    extra = 0


@admin.register(Cea)
class CeaAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = Cea
    extra_list_display = ('nit', 'name', 'manager', 'cellphone')
    inlines = [ScheduleAdmin, CeaLicenceAdmin, CeaVehicleAdmin, CeaRatingAdmin]

    manager_readonly_fields = ('manager', 'rating', 'collection', 'get_pin_sicov', 'get_recaudo' )
    readonly_fields = ('rating', 'get_pin_sicov', 'get_recaudo')

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )
    
    fieldsets = (
        (None, {
            'fields': ('name', 'nit', 'manager', 'phone', 'cellphone', 'email', 'logo', 'rating')
        }),
        ('Datos de ubicación', {
            'fields': ('state', 'city', 'sector', 'address'),
        }),
        ('Precios', {
            'fields': ('collection', 'get_pin_sicov', 'get_recaudo'),
        }),
    )

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django
        si el request.user es un usuario CEA, entonces solo muestra la
        empresa a la que pertenece
        """
        query = super(CeaAdmin, self).get_queryset(request)
        if request.user.user_type == User.ADMIN_CEA:
            try:
                return query.filter(manager=request.user)
            except Exception as e:
                print (e)
        else:
            return query.all()

    def get_readonly_fields(self, request, obj=None):
        if request.user.user_type == User.ADMIN_CEA:
            return self.manager_readonly_fields
        else:
            return super(CeaAdmin, self).get_readonly_fields(request, obj=obj)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "manager":
            kwargs["queryset"] = User.objects.filter(user_type='CEA', is_active=True).order_by('document_id')
        return super(CeaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Crc)
class CrcAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = Crc
    extra_list_display = ('nit', 'name', 'manager', 'cellphone')
    inlines = [ScheduleAdmin, CrcRatingAdmin]

    manager_readonly_fields = ('manager', 'collection', 'get_pin_sicov', 'get_recaudo', 'rating', )
    readonly_fields = ('rating', 'get_pin_sicov', 'get_recaudo')

    fieldsets = (
        (None, {
            'fields': ('name', 'nit', 'manager', 'phone', 'cellphone', 'email', 'logo', 'rating')
        }),
        ('Datos de ubicación', {
            'fields': ('state', 'city', 'sector', 'address'),
        }),
        ('Precios', {
            'fields': ('price', 'price_double', 'collection', 'get_pin_sicov', 'get_recaudo'),
        }),
    )

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )

    
    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django
        si el request.user es un usuario CEA, entonces solo muestra la
        empresa a la que pertenece
        """
        query = super(CrcAdmin, self).get_queryset(request)
        if request.user.user_type == User.ADMIN_CRC:
            try:
                return query.filter(manager=request.user)
            except Exception as e:
                print (e)
        else:
            return query.all()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "manager":
            kwargs["queryset"] = User.objects.filter(user_type='CRC', is_active=True).order_by('document_id')
        return super(CrcAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.user_type == User.ADMIN_CRC:
            return self.manager_readonly_fields
        else:
            return super(CrcAdmin, self).get_readonly_fields(request, obj=obj)
    
    def save_model(self, request, obj, form, change):
        if 'price' in form.changed_data or 'price_double' in form.changed_data:
            messages.warning(request, "Tus precios han cambiado. Recuerda reportar este cambio ante el ministerio de transporte de tu ciudad")
        super(CrcAdmin, self).save_model(request, obj, form, change)


@admin.register(TransitDepartment)
class TransitDepartmentAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = TransitDepartment
    extra_list_display = ('nit', 'name', 'cellphone')
    inlines = [ScheduleAdmin, TransitLicenceAdmin, TransitRatingAdmin]

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )


@admin.register(TuLicencia)
class TuLicenciaAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = TuLicencia
    extra_list_display = ('address', 'express_user', 'city', 'state')

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django
        si el request.user es un usuario CEA, entonces solo muestra la
        empresa a la que pertenece
        """
        query = super(TuLicenciaAdmin, self).get_queryset(request)
        if request.user.user_type == User.EXPRESS_USER:
            try:
                return query.filter(express_user=request.user)
            except Exception as e:
                print (e)
        else:
            return query.all()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "express_user":
            kwargs["queryset"] = User.objects.filter(user_type='EXU', is_active=True).order_by('document_id')
        return super(TuLicenciaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
