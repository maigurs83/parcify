from rest_framework import serializers
from .models import Parcel, ParcelLocker, Locker

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'

class ParcelLockerSerializer(serializers.ModelSerializer):
    lockers = LockerSerializer(many=True, read_only=True)

    class Meta:
        model = ParcelLocker
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
        read_only_fields = ('id','placedOn','updatedOn')
