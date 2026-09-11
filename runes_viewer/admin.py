from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from .models import Area, Place, Position, Runestone, TimePeriod


@admin.register(TimePeriod)
class TimePeriodAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'parish', 'area__text')
    search_fields = ('name', 'parish')

@admin.register(Runestone)
class RunestoneAdmin(gis_admin.GISModelAdmin):
    list_display = ('name', 'position__text', 'time_period__text', 'place__name')
    search_fields = ('name', 'place__name')

    fieldsets = (
        (None,
         {"fields": ["name", "description", "position", "time_period", "place", "location"]}),
        ("External Links",
         {"fields": ["fornsoek_url", "lantmaeteriet_url"]}),
        ("Media",
         {"fields": ["image",]}),
    )

    gis_widget_kwargs = {
        "attrs": {
            "display_raw": True,
            "default_lat": 57.7089,
            "default_lon": 11.9746,
            "default_zoom": 10,
        },
    }
