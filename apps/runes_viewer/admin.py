from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from .models import Area, Place, Position, Runestone, RunestonePosition, TimePeriod


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

class RunestonePositionInline(admin.TabularInline):
    model = RunestonePosition
    extra = 0

@admin.register(Place)
class PlaceAdmin(gis_admin.GISModelAdmin):
    list_display = ('name', 'parish', 'area__text')
    search_fields = ('name', 'parish')

    gis_widget_kwargs = {
        "attrs": {
            "display_raw": True,
            "default_lat": 57.7089,
            "default_lon": 11.9746,
            "default_zoom": 10,
        },
    }

@admin.register(Runestone)
class RunestoneAdmin(gis_admin.GISModelAdmin):
    list_display = ('name', 'time_period__text', 'place__name')
    search_fields = ('name', 'place__name')
    inlines = (RunestonePositionInline,)

    fieldsets = (
        (None,
         {"fields": ["name", "description", "time_period", "place", "coordinates"]}),
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

