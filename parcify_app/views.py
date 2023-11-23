from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Parcel, ParcelLocker, Locker
from .serializers import ParcelSerializer, ParcelLockerSerializer, LockerSerializer
from .services import ParcelService

class ParcelLockerViewSet(viewsets.ModelViewSet):
    queryset = ParcelLocker.objects.all()
    serializer_class = ParcelLockerSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def create(self, request, *args, **kwargs):
        serializer = ParcelSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)

        savedData = ParcelService.process_new_parcel(serializer.data)

        return Response(savedData, status=status.HTTP_201_CREATED)