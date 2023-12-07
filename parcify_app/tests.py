from django.test import TestCase
from .models import ParcelLocker
from .services import ParcelService

class ParcelServiceTests(TestCase):
    def setUp(self):
        # Create some sample ParcelLocker instances for testing
        ParcelLocker.objects.create(sizes="XS", status="Available", address="Locker A")
        ParcelLocker.objects.create(sizes="M", status="Available", address="Locker B")
        ParcelLocker.objects.create(sizes="L", status="Available", address="Locker C")

    def test_find_suitable_locker(self):
        # Test finding a suitable locker for a given size
        size = "M"
        suitable_locker = ParcelService.find_suitable_locker(size)

        self.assertEqual(suitable_locker.sizes, size)
        self.assertEqual(suitable_locker.status, "Available")

    def test_find_suitable_locker_no_match(self):
        # Test handling the case where no suitable locker is found
        size = "XL"
        
        with self.assertRaises(ValueError) as context:
            ParcelService.find_suitable_locker(size)

        self.assertIn("No suitable locker found", str(context.exception))

