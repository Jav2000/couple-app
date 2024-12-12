from django.contrib import admin

from .models import Trip

# Register your models here.
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'time_interval')  # Muestra el intervalo de fechas
    search_fields = ('destiny', 'description')
    list_filter = ('start_date', 'end_date')
