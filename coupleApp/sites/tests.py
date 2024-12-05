from django.test import TestCase
from datetime import date

from .models import Site, Photo

# Create your tests here.
# Make sure that you can create valid instances of the model Site
class SiteModelTestCase(TestCase):
    def test_create_site(self):
        site = Site.objects.create(
            name="Test Site",
            description="A test description.",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 12, 31),
            latitude=40.416775,
            longitude=-3.703790
        )
        self.assertEqual(Site.objects.count(), 1)
        self.assertEqual(site.name, "Test Site")
        self.assertEqual(site.time_interval(), "From 2023-01-01 to 2023-12-31")

# Check that errors are thrown if required fields are missing.
class RequiredFieldsTestCase(TestCase):
    def test_site_name_required(self):
        with self.assertRaises(Exception):
            Site.objects.create(
                description="Missing name.",
                start_date=date(2023, 1, 1),
                end_date=date(2023, 12, 31),
                latitude=40.416775,
                longitude=-3.703790
            )

# Verify that it does not allow saving a site with end_date before start_date
class SiteDateValidationTestCase(TestCase):
    def test_invalid_date_interval(self):
        with self.assertRaises(Exception) as context:
            Site.objects.create(
                name="Invalid Site",
                description="End date before start date.",
                start_date=date(2023, 12, 31),
                end_date=date(2023, 1, 1),
                latitude=40.416775,
                longitude=-3.703790
            )
        self.assertIn('The ending date cannot be before the starting date.', str(context.exception))

# Check that the time_interval method returns the expected string
class SiteMethodTestCase(TestCase):
    def test_time_interval(self):
        site = Site.objects.create(
            name="Test Interval",
            description="Testing time interval method.",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 12, 31),
            latitude=40.416775,
            longitude=-3.703790
        )
        self.assertEqual(site.time_interval(), "From 2023-01-01 to 2023-12-31")

# Verify that you can create a photo and that it is correctly associated with a site
class PhotoModelTestCase(TestCase):
    def setUp(self):
        self.site = Site.objects.create(
            name="Photo Site",
            description="Site for testing photos.",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 12, 31),
            latitude=40.416775,
            longitude=-3.703790
        )

    def test_create_photo(self):
        photo = Photo.objects.create(
            site=self.site,
            description="Test Photo",
            image="photos/2023/01/01/test.jpg"
        )
        self.assertEqual(Photo.objects.count(), 1)
        self.assertEqual(photo.site.name, "Photo Site")
        self.assertEqual(photo.description, "Test Photo")

# Verify that you can create a photo without associating it to a site
class PhotoOptionalSiteTestCase(TestCase):
    def test_create_photo_without_site(self):
        photo = Photo.objects.create(
            description="Photo without site",
            image="photos/2023/01/01/test.jpg"
        )
        self.assertEqual(photo.site, None)
        self.assertEqual(str(photo), "Photo from Not vinculated - Photo without site")

# Check that the image field stores the file path correctly
class PhotoImageFieldTestCase(TestCase):
    def test_image_field(self):
        photo = Photo.objects.create(
            description="Test Image",
            image="photos/2023/01/01/test_image.jpg"
        )
        self.assertEqual(photo.image.name, "photos/2023/01/01/test_image.jpg")

# Check that the photos are correctly linked to a site and are removed when the site is deleted
class SitePhotoRelationshipTestCase(TestCase):
    def setUp(self):
        self.site = Site.objects.create(
            name="Relationship Site",
            description="Testing relationships.",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 12, 31),
            latitude=40.416775,
            longitude=-3.703790
        )

    def test_photo_site_relationship(self):
        photo1 = Photo.objects.create(site=self.site, description="Photo 1")
        photo2 = Photo.objects.create(site=self.site, description="Photo 2")

        self.assertEqual(self.site.photos.count(), 2)
        self.assertIn(photo1, self.site.photos.all())
        self.assertIn(photo2, self.site.photos.all())

    def test_cascade_delete(self):
        Photo.objects.create(site=self.site, description="Photo to delete")
        self.assertEqual(Photo.objects.count(), 1)

        self.site.delete()
        self.assertEqual(Photo.objects.count(), 0)