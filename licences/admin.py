from django.contrib import admin

from .models import Licence

@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    """
    """

    model = Licence
    list_display = ('category',)

