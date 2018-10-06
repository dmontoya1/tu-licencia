
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from users.models import User
from .models import Request, LogRequestStatus, LogDocsStatus


class LogRequestStatusAdmin(admin.StackedInline):
    """
    """

    model = LogRequestStatus
    extra = 0
    readonly_fields = ('date', 'status')

    def has_add_permission(self, request):
        return False
    
    # def has_delete_permission(self, request, ob=None):
    #     return False


class LogDocsStatusAdmin(admin.StackedInline):
    """
    """

    model = LogDocsStatus
    extra = 0
    readonly_fields = ('date', 'status',)


    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, ob=None):
        return False

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """
    """

    model = Request
    search_fields = ('cea__name', 'crc__name', 'transit__name', 'user__document_id', 'user__first_name',
    'user__last_name', 'request_status', 'payment_type', 'request_date', 'cea_status', 'crc_status')

    readonly_fields = ('booking', 'get_crc_price', 'request_date') #Eliminar esta linea y dejar la de abajo
    # readonly_fields = ('booking', 'user', 'licences', 'get_crc_price', 'request_date)

    inlines = [LogRequestStatusAdmin, LogDocsStatusAdmin, ]
    
    def changelist_view(self, request, extra_context=None):
        """
        funcion para cambiar los nombres a mostrar para las solicitudes dependiendo del tipo de usuario registrado
        """
        if request.user.user_type == User.ADMIN_CEA:
            self.list_display = ('user', 'cea', 'booking')
        elif request.user.user_type == User.ADMIN_CRC:
            self.list_display = ('user', 'crc', 'booking')
        elif request.user.user_type == User.EXPRESS_USER:
            self.list_display = ('user', 'payment_type', 'request_status', 'credit_status', 'booking')
        else:
            self.list_display = ('user', 'booking','cea', 'crc', 'transit', 'payment_type', 'request_status',)
        return super(RequestAdmin, self).changelist_view(request, extra_context)
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type=User.CLIENTE)
        return super(RequestAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    fieldsets = (
        (None,
         {'fields':
          ('user', 'payment_type', 'request_status', 'docs_status', 'credit_status', 'credit_request_code', 'booking', 'request_date')}),
        (_('CRC'), {'fields': ('crc', 'crc_status',)}),
        (_('CEA'), {'fields': ('cea', 'licences', 'cea_status', )}),
        (_('Transito'), {'fields': ('transit',)})
    )
    cea_fieldsets = (
        (None, {
            'fields': ('user', 'cea', 'booking', 'licences', 'request_status', 'request_date', 'cea_status')
        }),
    )
    crc_fieldsets = (
        (None, {
            'fields': ('user', 'crc', 'booking', 'licences', 'request_status', 'request_date', 'crc_status')
        }),
    )
    exp_fieldsets = (
        (None, {
            'fields': ('user', 'request_status', 'payment_type', 'credit_status', 'credit_request_code', 'booking', 'licences', 'request_date',)
        }),
    )

    cea_readonly_fields = ('user', 'cea', 'booking', 'licences', 'request_status', 'request_date',)
    crc_readonly_fields = ('user', 'crc', 'booking', 'licences', 'request_status', 'request_date',)


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
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.user_type == User.ADMIN_CEA:
            return self.cea_readonly_fields
        elif request.user.user_type == User.ADMIN_CRC:
            return self.crc_readonly_fields
        # elif request.user.user_type == User.EXPRESS_USER:
        #     return self.exp_fieldsets
        else:
            return super(RequestAdmin, self).get_readonly_fields(request, obj=obj)

