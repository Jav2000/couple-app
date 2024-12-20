from django.db import models
from django.forms import ValidationError

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owned = models.BooleanField(default=False)
    brand = models.CharField(max_length=100, blank=True, null=True)

    CATEGORY_CHOICES = [
        ('Rostro', 'Rostro'),
        ('Ojos', 'Ojos'),
        ('Labios', 'Labios'),
        ('Manos', 'Manos'),
        ('Paletas', 'Paletas'),
    ]

    SUBCATEGORY_CHOICES = {
        'Rostro': [
            ('bases_maquillaje', 'Bases de maquillaje'),
            ('colorete', 'Colorete'),
            ('bronceadores', 'Bronceadores y contouring'),
            ('correctores', 'Correctores'),
            ('iluminadores', 'Iluminadores'),
            ('fijadores', 'Fijadores'),
            ('polvos', 'Polvos'),
            ('prebases_rostro', 'Prebases'),
        ],
        'Ojos': [
            ('mascaras', 'Máscaras'),
            ('sombras', 'Sombras de ojos'),
            ('lapices', 'Lápices de ojos'),
            ('cejas', 'Cejas'),
            ('delineadores', 'Delineadores'),
            ('prebases_ojos', 'Prebases para ojos'),
        ],
        'Labios': [
            ('labiales', 'Labiales'),
            ('brillos_labios', 'Brillos de labios'),
            ('lapices_contorno', 'Lápices contorno'),
            ('prebases_labios', 'Prebases para labios'),
        ],
        'Manos': [
            ('esmaltes', 'Esmaltes de uñas'),
            ('cuidado_unas', 'Cuidado de las uñas'),
            ('manicura_francesa', 'Manicura francesa'),
            ('quitaesmaltes', 'Quitaesmaltes'),
            ('fijadores_esmalte', 'Fijadores de esmalte de uñas'),
        ],
        'Paletas': [
            ('paletas_rostro', 'Paletas para rostro'),
            ('paletas_ojos', 'Paletas para ojos'),
        ],
    }

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=50, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='makeup_item_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def clean(self):
        # Validación personalizada para las subcategorías
        if self.category and self.subcategory:
            valid_subcategories = dict(self.SUBCATEGORY_CHOICES).get(self.category, [])
            if not any(choice[0] == self.subcategory for choice in valid_subcategories):
                raise ValidationError({'subcategory': 'Subcategoría no válida para la categoría seleccionada.'})

    def get_subcategories(self):
        return self.SUBCATEGORY_CHOICES.get(self.category, [])

    def __str__(self):
        return self.name