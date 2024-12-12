from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from sites.models import Site, Photo
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

class SiteViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.site = Site.objects.create(
            name="Test Site",
            description="A test site description.",
            start_date="2023-01-01",
            end_date="2023-12-31",
            latitude=40.416775,
            longitude=-3.703790,
        )
    
    def test_sites_page(self):
        response = self.client.get(reverse('sites:sites_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sites_page.html')
        self.assertIn('sites', response.context)

    def test_site_details_page(self):
        response = self.client.get(reverse('sites:site_details_page', args=[self.site.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site_details_page.html')
        self.assertIn('site', response.context)
        self.assertEqual(response.context['site'], self.site)

    def test_sites_geojson(self):
        response = self.client.get(reverse('sites:sites_geojson'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        geojson_data = response.json()
        self.assertEqual(geojson_data['type'], 'FeatureCollection')
        self.assertEqual(len(geojson_data['features']), 1)
        self.assertEqual(geojson_data['features'][0]['properties']['name'], self.site.name)

    def test_get_google_maps_key(self):
        response = self.client.get(reverse('sites:get_google_maps_key'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json().get('apiKey'), settings.GOOGLE_MAPS_API_KEY)

    def test_new_site(self):
        form_data = {
            'name': 'New Site',
            'description': 'New description',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'latitude': 41.0,
            'longitude': -3.5,
        }
        response = self.client.post(reverse('sites:new_site'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Site.objects.count(), 2)
    
    def test_edit_site(self):
        new_name = "Updated Site Name"
        form_data = {
            'name': new_name,
            'description': self.site.description,
            'start_date': self.site.start_date,
            'end_date': self.site.end_date,
            'latitude': self.site.latitude,
            'longitude': self.site.longitude,
        }
        response = self.client.post(reverse('sites:edit_site', args=[self.site.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirección
        self.site.refresh_from_db()
        self.assertEqual(self.site.name, new_name)

    def test_delete_site(self):
        response = self.client.post(reverse('sites:delete_site', args=[self.site.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Site.objects.count(), 0)

    def test_add_photos(self):
        image_data = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('sites:add_photos', args=[self.site.pk]), {'image': image_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.count(), 1)

    def test_delete_photo(self):
        photo = Photo.objects.create(site=self.site, image="test.jpg")
        response = self.client.delete(reverse('sites:delete_photo', args=[photo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Photo.objects.count(), 0)