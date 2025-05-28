from django.db import models
from django.forms import ValidationError

# Create your models here.
class SkincareProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owned = models.BooleanField(default=False)
    brand = models.CharField(max_length=100, blank=True, null=True)

    CATEGORY_CHOICES = [
        ('Limpiadores', 'Limpiadores'),
        ('Tonicos', 'Tónicos'),
        ('Serums', 'Serums'),
        ('Crema_hidratante', 'Crema hidratante'),
        ('Contorno_de_ojos', 'Contorno de ojos'),
        ('Exfoliantes', 'Exfoliantes'),
        ('Tratamiento_de_labios', 'Tratamiento de labios'),
        ('Desmaquillantes', 'Desmaquillantes'),
        ('Mascarillas', 'Mascarillas'),
    ]

    category = models.CharField(max_length=21, choices=CATEGORY_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='skincare_product_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name