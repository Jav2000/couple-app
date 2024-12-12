from django.test import TestCase
from django.core.exceptions import ValidationError
from trips.models import Trip
from datetime import date

class TripModelTests(TestCase):
    def setUp(self):
        # Crear un sitio inicial para pruebas
        self.trip = Trip.objects.create(
            destiny="Paris",
            description="A romantic city",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 10),
            latitude=48.8566,
            longitude=2.3522
        )

    def test_string_representation(self):
        self.assertEqual(str(self.trip), "Paris")

    def test_time_interval_method(self):
        self.assertEqual(self.trip.time_interval(), "From 2023-01-01 to 2023-01-10")

    def test_clean_method_invalid_dates(self):
        with self.assertRaises(ValidationError):
            trip = Trip(
                destiny="Invalid Dates",
                description="Testing invalid dates",
                start_date=date(2023, 1, 10),
                end_date=date(2023, 1, 1),
                latitude=0.0,
                longitude=0.0
            )
            trip.full_clean()  # Llama a clean para validar los datos

    def test_save_calls_clean(self):
        with self.assertRaises(ValidationError):
            trip = Trip(
                destiny="Invalid Save",
                description="Testing save with invalid dates",
                start_date=date(2023, 1, 10),
                end_date=date(2023, 1, 1),
                latitude=0.0,
                longitude=0.0
            )
            trip.save()  # Esto debería fallar porque llama a full_clean