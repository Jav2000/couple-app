from django.db import models

from trips.models import Trip

# Create your models here.
class Photo(models.Model):
    trip = models.ForeignKey(Trip, related_name="photos", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo from {self.trip.destiny if self.trip else 'Not vinculated'} - {self.description}"
