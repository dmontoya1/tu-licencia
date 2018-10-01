
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from users.models import User
from .models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """
    """

    model = Request
    search_fields = ('cea__name', 'crc__name', 'transit__name', 'user__document_id', 'user__first_name',
    'user__last_name', 'status', 'payment_type')

    readonly_fields = ('get_crc_price', 'request_date') #Eliminar esta linea y dejar la de abajo
    # readonly_fields = ('cea', 'crc', 'transit', 'user', 'licences', 'get_crc_price', 'request_date)
    
    def changelist_view(self, request, extra_context=None):
        """
        funcion para cambiar los nombres a mostrar para las solicitudes dependiendo del tipo de usuario registrado
        """
        if request.user.user_type == User.ADMIN_CEA:
            self.list_display = ('user', 'cea', 'booking')
        elif request.user.user_type == User.ADMIN_CRC:
            self.list_display = ('user', 'crc', 'booking')
        elif request.user.user_type == User.EXPRESS_USER:
            self.list_display = ('user', 'payment_type', 'status', 'credit_status', 'booking')
        else:
            self.list_display = ('cea', 'crc', 'transit', 'user', 'payment_type', 'status', 'booking')
        return super(RequestAdmin, self).changelist_view(request, extra_context)
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type=User.CLIENTE)
        return super(RequestAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    fieldsets = (
        (None,
         {'fields':
          ('user', 'payment_type', 'status', 'credit_status', 'credit_request_code', 'booking', 'request_date')}),
        (_('CEA'), {'fields': ('cea', 'licences', )}),
        (_('CRC'), {'fields': ('crc', )}),
        (_('Transito'), {'fields': ('transit',)})
    )
    cea_fieldsets = (
        (None, {
            'fields': ('user', 'cea', 'booking', 'licences', 'status', 'credit_status', 'request_date')
        }),
    )
    crc_fieldsets = (
        (None, {
            'fields': ('user', 'crc', 'licences', 'booking', 'request_date')
        }),
    )
    exp_fieldsets = (
        (None, {
            'fields': ('user', 'payment_type', 'credit_status', 'credit_request_code', 'booking', 'licences', 'request_date')
        }),
    )


    def get_fieldsets(self, request, obj=None):
        """
        Hook for specifying fieldsets.
        """
        if request.user.user_type == User.ADMIN_CEA:
            return self.cea_fieldsets
        elif request.user.user_type == User.ADMIN_CRC:
            return self.crc_fieldsets
        elif request.user.user_type == User.EXPRESS_USER:
            return self.exp_fieldsets
        return self.fieldsets
    

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django
        si el request.user es un usuario CEA, entonces solo muestra la
        empresa a la que pertenece
        """
        query = super(RequestAdmin, self).get_queryset(request)
        if request.user.user_type == User.ADMIN_CEA:
            return query.filter(cea=request.user.cea)
        elif request.user.user_type == User.ADMIN_CRC:
            return query.filter(crc=request.user.crc)
        else:
            return query.all()


