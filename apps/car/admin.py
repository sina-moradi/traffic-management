from django.contrib import admin
from .models.toll_station import TollStation, Road
from .models.car import Car, Positioning
from .models.owner import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'national_code']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['length', 'type']


@admin.register(Positioning)
class PositioningAdmin(admin.ModelAdmin):
    list_display = ['car', 'location', 'date']


@admin.register(TollStation)
class TollStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'toll_per_station', 'location']


@admin.register(Road)
class TollStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'width', 'geom']