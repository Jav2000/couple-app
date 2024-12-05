from django.contrib import admin

from .models import Site, Photo

# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_interval')  # Muestra el intervalo de fechas
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('site', 'image', 'description')  # Asegúrate de incluir los campos que quieres mostrar
    search_fields = ('site',)  # Permite buscar fotos por nombre de sitio
    list_filter = ('site', 'date_added')  # Filtros para facilitar la búsqueda
