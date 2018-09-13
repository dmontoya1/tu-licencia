from django.contrib import admin

from .models import Brand, Vehicle, VehicleImages


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    """

    model = Brand
    list_display = ("name",)


class VehicleImagesAdmin(admin.TabularInline):
    """
    """

    model = VehicleImages
    extra = 0


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """
    """

    model = Vehicle
    list_display = ("line", 'brand',)
    inlines = [VehicleImagesAdmin, ]
