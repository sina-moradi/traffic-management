from rest_framework import serializers

from .models.car import Car, Positioning, CarToll
from .models.owner import Owner


class OwnerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'age')


class OwnerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'national_code')


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


class PositioningSerializers(serializers.ModelSerializer):
    class Meta:
        model = Positioning
        fields = '__all__'


class CarTollTimeSerializers(serializers.Serializer):

    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()


class CarTollSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarToll
        fields = '__all__'
