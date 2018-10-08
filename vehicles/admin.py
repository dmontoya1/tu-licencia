from django.contrib import admin

from utils.admin import SoftDeletionModelAdminMixin
from .models import Brand, Vehicle, VehicleImages


@admin.register(Brand)
class BrandAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = Brand
    extra_list_display = ("name",)


class VehicleImagesAdmin(admin.TabularInline):
    """
    """

    model = VehicleImages
    extra = 0


@admin.register(Vehicle)
class VehicleAdmin(SoftDeletionModelAdminMixin):
    """
    """

    model = Vehicle
    extra_list_display = ("line", 'brand',)
    inlines = [VehicleImagesAdmin, ]
