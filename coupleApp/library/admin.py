from django.contrib import admin

from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publish_date')  # Campos a mostrar en la lista de libros
    list_filter = ('genre', 'publish_date')  # Filtros por género y fecha de publicación
    search_fields = ('title', 'author')  # Permite buscar por título y autor
    ordering = ('-publish_date',)  # Ordenar los libros por la fecha de publicación en orden descendente