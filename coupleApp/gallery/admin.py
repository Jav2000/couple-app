from django.contrib import admin

from .models import Photo

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('trip', 'image', 'description')  # Asegúrate de incluir los campos que quieres mostrar
    search_fields = ('trip',)  # Permite buscar fotos por nombre de sitio
    list_filter = ('trip', 'date_added')  # Filtros para facilitar la búsqueda