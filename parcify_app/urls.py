from django.urls import path, include
from rest_framework import routers
from .views import ParcelViewSet, ParcelLockerViewSet

router = routers.DefaultRouter()
router.register(r'parcels', ParcelViewSet)
router.register(r'parcel_lockers', ParcelLockerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    #path('', AppView.as_view(), name='app'),
]
