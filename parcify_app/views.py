from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Parcel, ParcelLocker, Locker
from .serializers import ParcelSerializer, ParcelLockerSerializer, LockerSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class ParcelLockerViewSet(viewsets.ModelViewSet):
    queryset = ParcelLocker.objects.all()
    serializer_class = ParcelLockerSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
