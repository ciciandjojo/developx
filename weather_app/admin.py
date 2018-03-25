from django.contrib import admin

from .models import GeoPosition, WeatherEntry, AverageStats


@admin.register(GeoPosition)
class GeoPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'coordinates', 'height']


@admin.register(WeatherEntry)
class WeatherEntryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in WeatherEntry._meta.get_fields()]


@admin.register(AverageStats)
class AverageStatsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in AverageStats._meta.get_fields()]
