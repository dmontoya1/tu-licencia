
from django.contrib import admin

from users.models import User
from .models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """
    """

    model = Request
    search_fields = ('cea__name', 'crc__name', 'transit_name', 'user__document_id', 'status', 'payment_type')

    readonly_fields = ('get_crc_price', ) #Eliminar esta linea y dejar la de abajo
    # readonly_fields = ('cea', 'crc', 'transit', 'user', 'licences', 'get_crc_price')
    
    def changelist_view(self, request, extra_context=None):
        """
        funcion para cambiar los nombres a mostrar para las solicitudes dependiendo del tipo de usuario registrado
        """
        if request.user.user_type == User.ADMIN_CEA:
            self.list_display = ('user', 'cea')
        elif request.user.user_type == User.ADMIN_CRC:
            self.list_display = ('user', 'crc')
        elif request.user.user_type == User.EXPRESS_USER:
            self.list_display = ('user', 'payment_type', 'status', 'credit_status')
        else:
            self.list_display = ('cea', 'crc', 'transit', 'user', 'payment_type', 'status', 'credit_status')
        return super(RequestAdmin, self).changelist_view(request, extra_context)
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type=User.CLIENTE)
        return super(RequestAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    

    cea_fieldsets = (
        (None, {
            'fields': ('cea', 'user', 'licences')
        }),
    )
    crc_fieldsets = (
        (None, {
            'fields': ('crc', 'user', 'licences')
        }),
    )
    exp_fieldsets = (
        (None, {
            'fields': ('user', 'credit_status', )
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
        return [(None, {'fields': self.get_fields(request, obj)})]


