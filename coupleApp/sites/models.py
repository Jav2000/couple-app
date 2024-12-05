from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
    def time_interval(self):
        return f"From {self.start_date} to {self.end_date}"
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('The ending date cannot be before the starting date.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class Photo(models.Model):
    site = models.ForeignKey(Site, related_name="photos", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo from {self.site.name if self.site else 'Not vinculated'} - {self.description}"

