from django.contrib import admin
from .models.toll_station import TollStation, Road
from .models.car import Car, Positioning, CarToll
from .models.owner import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'national_code']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['owner', 'length', 'type', 'color', 'load_volume']


@admin.register(Positioning)
class PositioningAdmin(admin.ModelAdmin):
    list_display = ['car', 'location', 'date']


@admin.register(TollStation)
class TollStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'toll_per_station', 'location']


@admin.register(Road)
class TollStationAdmin(admin.ModelAdmin):
    list_display = ['name', 'width', 'geom']


@admin.register(CarToll)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car', 'toll', 'date']