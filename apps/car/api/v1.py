from rest_framework import generics

from apps.car.models.car import Car
from apps.car.models.owner import Owner
from apps.car.serializers import CarListSerializers, OwnerCreateSerializers, CarCreateSerializers


class ColorFullCarListAPIView(generics.ListAPIView):
    serializer_class = CarListSerializers

    def get_queryset(self):
        colors = ['red', 'blue']
        queryset = Car.objects.filter(color__in=colors)
        return queryset


class HeavyCarListAPIView(generics.ListAPIView):
    serializer_class = CarListSerializers

    def get_queryset(self):
        queryset = Car.objects.filter(type='b', positions__location__width__gte=20.0)
        return queryset


class OwnerAgeFilterListAPIView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.filter(owner__age__gt=70)


class OwnerCreateAPIView(generics.CreateAPIView):

    serializer_class = OwnerCreateSerializers
    queryset = Owner.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializers
