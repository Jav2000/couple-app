from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from trips.models import Trip
from gallery.models import Photo
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

class TripsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.trip = Trip.objects.create(
            destiny="Test Trip",
            description="A test trip description.",
            start_date="2023-01-01",
            end_date="2023-12-31",
            latitude=40.416775,
            longitude=-3.703790,
        )
    
    def test_trips_page(self):
        response = self.client.get(reverse('trips:trips_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips_page.html')
        self.assertIn('trips', response.context)

    def test_trip_details_page(self):
        response = self.client.get(reverse('trips:trip_details_page', args=[self.trip.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trip_details_page.html')
        self.assertIn('trip', response.context)
        self.assertEqual(response.context['trip'], self.trip)

    def test_trips_geojson(self):
        response = self.client.get(reverse('trips:trips_geojson'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        geojson_data = response.json()
        self.assertEqual(geojson_data['type'], 'FeatureCollection')
        self.assertEqual(len(geojson_data['features']), 1)
        self.assertEqual(geojson_data['features'][0]['properties']['destiny'], self.trip.destiny)

    def test_get_google_maps_key(self):
        response = self.client.get(reverse('trips:get_google_maps_key'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json().get('apiKey'), settings.GOOGLE_MAPS_API_KEY)

    def test_new_trip(self):
        form_data = {
            'destiny': 'New Trip',
            'description': 'New description',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'latitude': 41.0,
            'longitude': -3.5,
        }
        response = self.client.post(reverse('trips:new_trip'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Trip.objects.count(), 2)
    
    def test_edit_trip(self):
        new_destiny = "Updated Trip Name"
        form_data = {
            'destiny': new_destiny,
            'description': self.trip.description,
            'start_date': self.trip.start_date,
            'end_date': self.trip.end_date,
            'latitude': self.trip.latitude,
            'longitude': self.trip.longitude,
        }
        response = self.client.post(reverse('trips:edit_trip', args=[self.trip.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirección
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.destiny, new_destiny)

    def test_delete_trip(self):
        response = self.client.post(reverse('trips:delete_trip', args=[self.trip.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trip.objects.count(), 0)

    def test_add_trip_photos(self):
        image_data = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('trips:add_trip_photos', args=[self.trip.pk]), {'image': image_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.count(), 1)

    def test_delete_photo(self):
        photo = Photo.objects.create(trip=self.trip, image="test.jpg")
        response = self.client.delete(reverse('trips:delete_trip_photo', args=[photo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.count(), 0)