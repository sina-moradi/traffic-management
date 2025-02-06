from rest_framework import serializers

from .models.car import Car
from .models.owner import Owner


class OwnerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name',)


class CarListSerializers(serializers.ModelSerializer):
    owner = OwnerNameSerializer()

    class Meta:
        model = Car
        fields = ('type', 'color', 'length', 'load_volume', 'owner')


class OwnerCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'age', 'national_code')


class CarCreateSerializers(serializers.ModelSerializer):
    type = serializers.CharField(required=True)

    class Meta:
        model = Car
        fields = ('color', 'type', 'length', 'owner', 'load_volume')