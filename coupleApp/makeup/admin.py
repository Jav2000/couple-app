from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'owned', 'created_at', 'updated_at')
    list_filter = ('category', 'owned', 'brand')
    search_fields = ('name', 'brand', 'category')