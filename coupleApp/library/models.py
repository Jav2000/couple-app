from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Título del libro (obligatorio)
    author = models.CharField(max_length=200)  # Autor del libro (obligatorio)
    description = models.TextField(blank=True, null=True)  # Descripción (opcional)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)  # ISBN (opcional)
    genre = models.CharField(max_length=100, blank=True, null=True)  # Género (opcional)
    publish_date = models.DateField(null=True, blank=True)  # Fecha de publicación (opcional)
    pages = models.PositiveIntegerField(blank=True, null=True)  # Número de páginas (opcional)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Imagen de la portada (opcional)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def __str__(self):
        return self.title