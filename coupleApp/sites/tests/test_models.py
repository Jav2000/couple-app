from django.test import TestCase
from django.core.exceptions import ValidationError
from sites.models import Site, Photo
from datetime import date

class SiteModelTests(TestCase):
    def setUp(self):
        # Crear un sitio inicial para pruebas
        self.site = Site.objects.create(
            name="Paris",
            description="A romantic city",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 10),
            latitude=48.8566,
            longitude=2.3522
        )

    def test_string_representation(self):
        self.assertEqual(str(self.site), "Paris")

    def test_time_interval_method(self):
        self.assertEqual(self.site.time_interval(), "From 2023-01-01 to 2023-01-10")

    def test_clean_method_invalid_dates(self):
        with self.assertRaises(ValidationError):
            site = Site(
                name="Invalid Dates",
                description="Testing invalid dates",
                start_date=date(2023, 1, 10),
                end_date=date(2023, 1, 1),
                latitude=0.0,
                longitude=0.0
            )
            site.full_clean()  # Llama a clean para validar los datos

    def test_save_calls_clean(self):
        with self.assertRaises(ValidationError):
            site = Site(
                name="Invalid Save",
                description="Testing save with invalid dates",
                start_date=date(2023, 1, 10),
                end_date=date(2023, 1, 1),
                latitude=0.0,
                longitude=0.0
            )
            site.save()  # Esto debería fallar porque llama a full_clean

class PhotoModelTests(TestCase):
    def setUp(self):
        # Crear un sitio y una foto inicial para pruebas
        self.site = Site.objects.create(
            name="London",
            description="Historic city",
            start_date=date(2023, 5, 1),
            end_date=date(2023, 5, 15),
            latitude=51.5074,
            longitude=-0.1278
        )
        self.photo = Photo.objects.create(
            site=self.site,
            image="photos/2023/05/01/photo1.jpg",
            description="Big Ben photo"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.photo), "Photo from London - Big Ben photo")

    def test_photo_without_site(self):
        photo = Photo.objects.create(
            image="photos/2023/05/01/photo2.jpg",
            description="Independent photo"
        )
        self.assertEqual(str(photo), "Photo from Not vinculated - Independent photo")