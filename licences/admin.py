from django.contrib import admin

from .models import Licence, AgeRange, AnsvRanges

@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    """
    """

    model = Licence
    list_display = ('category',)


@admin.register(AgeRange)
class AgeRangeAdmin(admin.ModelAdmin):
    """
    """

    model = AgeRange
    list_display = ('start_age', 'end_age')


@admin.register(AnsvRanges)
class AnsvRangesAdmin(admin.ModelAdmin):
    """
    """

    model = AnsvRanges
    list_display = ('gender', 'age_range', 'price', 'licence')
