from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.db.models import Sum

from apps.car.models.car import Car, Positioning, CarToll
from apps.car.models.owner import Owner
from apps.car.serializers import CarListSerializers, OwnerCreateSerializers, CarCreateSerializers, OwnerInfoSerializer,\
    PositioningSerializers, CarTollSerializers, CarTollTimeSerializers


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


class OwnerInfoListAPIView(generics.ListAPIView):
    serializer_class = OwnerInfoSerializer
    queryset = Owner.objects.filter(cars__tolls__isnull=False).annotate(
        total_toll=Sum('cars__tolls__toll')
    ).order_by('total_toll')
    print(queryset)


class PositionCarAPIView(generics.ListAPIView):

    center_point = Point(51.3890, 35.6892)
    radius = D(m=600)
    serializer_class = PositioningSerializers
    queryset = Positioning.objects.filter(location__distance_lte=(center_point, radius), car__type='s')


class CarTollsAPIView(APIView):
    def post(self, request, pk):
        ser_data = CarTollTimeSerializers(data=request.data)
        if ser_data.is_valid():
            queryset = CarToll.objects.filter(car_id=pk, date__range=(ser_data.data['start_time'],
                                                                      ser_data.data['end_time']))
            tolls = CarTollSerializers(queryset, many=True).data
            return Response(data=tolls)
        return Response(ser_data.errors, status=400)
