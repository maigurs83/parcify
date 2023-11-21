from django.db import models

"""

Company provides a parcel locker service.

We need a simple Python webservice that would allow us to work with 2 entities: 
* a parcel to be delivered. You can decide the fields to describe the parcel, what makes sense in your opinion.
parcel_locker 
* again, feel free to pick the fields which are relevant in your opinion.
Parcel is supposed to have at least information about the sender, receiver, size of the parcel (e.g. XS/S/M/L/XL), information about the locker it’s stored at.
Locker would require information about relevant sizes (see parcel), status of the locker, address of a locker.
We need REST API methods for CRUD operations on parcels and parcel lockers.
Methods should persist data in database (any of your choice). Implement validations that would be appropriate. 

"""

class Parcel(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')])
    paid = models.BooleanField(default=False, blank=False)
    placedOn = models.DateTimeField(auto_now_add=True, blank=False)
    updatedOn = models.DateTimeField(blank=True)
    status = models.CharField(max_length=20, choices=[('Placed', 'Order has made'), ('Preparing', 'At storage house'), ('Arriving', 'Riding to the locker'), ('Arrived', 'Waiting at the parcel locker'), ('Delivered', 'Found new home')])
    locker = models.ForeignKey('Locker', on_delete=models.DO_NOTHING, default=0)

class ParcelLocker(models.Model):
    sizes = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Open', 'Available lockers left'), ('Maintanence', 'Not available'), ('Closed', 'No lockers left')])
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField()

class Locker(models.Model):
    parcelLocker = models.ForeignKey('ParcelLocker', related_name='lockers', on_delete=models.CASCADE)       
    size = models.CharField(max_length=2, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')])
    empty = models.BooleanField(default=True, blank=False) 
