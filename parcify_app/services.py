from django.utils import timezone
from .models import Locker
from .serializers import ParcelSerializer

class ParcelService:
    @staticmethod
    def process_new_parcel(parcel_data):        
        size = parcel_data.get('size')
        parcelLockerId = parcel_data.get('locker')

        locker = ParcelService.find_suitable_locker(size, parcelLockerId)

        parcel_data['locker'] = locker.id
        parcel_data['placedOn'] = timezone.now()
        parcel_data['updatedOn'] = timezone.now()
        parcel_data['status'] = 'Placed'

        serializer = ParcelSerializer(data=parcel_data)
        serializer.is_valid(raise_exception=True)
        saved_instance = serializer.save()
        print(f"Notification: Parcel has been created with size {size}.")

        return parcel_data

    @staticmethod
    def find_suitable_locker(size, parcelLockerId):
        locker = Locker.objects.filter(parcelLocker__exact=parcelLockerId,size__exact=size,empty__exact=True).first()

        if not locker:
            raise ValueError(f"No suitable locker found for parcel size: {size}")

        return locker
