from django.shortcuts import render
from .models import Photo

# Create your views here.
def photo_gallery(request):
    photos = Photo.objects.select_related('trip').order_by('-date_added')  # Ordenar por fecha descendente
    return render(request, 'photo_gallery.html', {'photos': photos})