from django.test import TestCase
from django.core.exceptions import ValidationError
from trips.models import Trip
from gallery.models import Photo
from datetime import date

class PhotoModelTests(TestCase):
    def setUp(self):
        # Crear un sitio y una foto inicial para pruebas
        self.trip = Trip.objects.create(
            destiny="London",
            description="Historic city",
            start_date=date(2023, 5, 1),
            end_date=date(2023, 5, 15),
            latitude=51.5074,
            longitude=-0.1278
        )
        self.photo = Photo.objects.create(
            trip=self.trip,
            image="photos/2023/05/01/photo1.jpg",
            description="Big Ben photo"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.photo), "Photo from London - Big Ben photo")

    def test_photo_without_trip(self):
        photo = Photo.objects.create(
            image="photos/2023/05/01/photo2.jpg",
            description="Independent photo"
        )
        self.assertEqual(str(photo), "Photo from Not vinculated - Independent photo")