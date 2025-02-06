from rest_framework import generics

from apps.car.models.car import Car
from apps.car.serializers import CarListSerializers


class ColorFullCarListAPIView(generics.ListAPIView):
    serializer_class = CarListSerializers

    def get_queryset(self):
        colors = ['red', 'blue']
        queryset = Car.objects.filter(color__in=colors)
        return queryset
