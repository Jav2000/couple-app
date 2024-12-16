from django.db import models
from django.utils.text import slugify

from trips.models import Trip

from datetime import datetime
import os

def trip_photo_upload_to(instance, filename):
    today = datetime.now()
    date_path = today.strftime('%Y/%m/%d')

    ext = filename.split('.')[-1]

    base_filename = slugify(instance.trip.destiny)

    existing_photo_count = instance.trip.photos.count()

    unique_suffix = f"{existing_photo_count + 1}_{datetime.now().strftime('%f')}"

    new_filename = f"{base_filename}_{unique_suffix}.{ext}"

    return os.path.join('photos', date_path, new_filename)

# Create your models here.
class Photo(models.Model):
    trip = models.ForeignKey(Trip, related_name="photos", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=trip_photo_upload_to)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo from {self.trip.destiny if self.trip else 'Not vinculated'} - {self.description}"
