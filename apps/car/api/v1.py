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


class OwnerCreateAPIView(generics.CreateAPIView):

    serializer_class = OwnerCreateSerializers
    queryset = Owner.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializers
