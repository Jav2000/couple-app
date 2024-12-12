from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Trip(models.Model):
    destiny = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.destiny
    
    def time_interval(self):
        return f"From {self.start_date} to {self.end_date}"
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('The ending date cannot be before the starting date.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
