from rest_framework import serializers

from .models.car import Car


class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
