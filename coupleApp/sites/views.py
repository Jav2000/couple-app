from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import Site, Photo
from .forms import SiteForm

import os

# Create your views here.
def sites_page(request):
    sites = Site.objects.all()
    return render(request, 'sites_page.html', {'sites': sites})

def site_details_page(request, pk):
    site = get_object_or_404(Site, pk=pk)
    return render(request, 'site_details_page.html', {'site': site})

def sites_geojson(request):
    sites = Site.objects.all()
    features = []

    for site in sites:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [site.longitude, site.latitude]
            },
            "properties": {
                "name": site.name,
                "description": site.description,
                "pk": site.pk
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return JsonResponse(geojson)

def get_google_maps_key(request):
    return JsonResponse({'apiKey': settings.GOOGLE_MAPS_API_KEY})

def new_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo sitio en la base de datos
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = SiteForm()

    return render(request, 'new_site.html', {'form': form})

def edit_site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('sites:site_details_page', pk=pk)
    else:
        form = SiteForm(instance=site)
    return render(request, 'edit_site.html', {'form': form, 'site': site})

def delete_site(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method == 'POST':
        site.delete()
        return redirect('sites:sites_page')
    return render(request, 'delete_confirmation.html', {'site': site})

def add_photos(request, pk):
    site = get_object_or_404(Site, pk=pk)

    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'success': False, 'message': 'The file is not getting to the server.'}, status=400)
        
        image = request.FILES['image']
        response_data = []

        try:
            if image.size > 5 * 1024 * 1024:  # Limitar tamaño del archivo a 5MB
                raise ValidationError("El archivo es demasiado grande.")
            
            photo = Photo(image=image, site=site)  # Crea una nueva instancia de Photo
            photo.save()  # Guarda la foto en la base de datos
            response_data.append({
                'photo_url': photo.image.url,
                'success': True,
            })
            return JsonResponse(response_data, safe=False)
        except ValidationError as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Ocurrió un error al guardar las fotos.'}, status=500)
    else:
        return render(request, 'add_photos.html', {'site': site})

def delete_photo(request, photo_id):
    if request.method == 'DELETE':  # Solo permitir el método DELETE
        try:
            photo = get_object_or_404(Photo, pk=photo_id)
            photo_path = photo.image.path if photo.image else None

            photo.delete()

            if photo_path and os.path.exists(photo_path):
                os.remove(photo_path)
                return JsonResponse({'message': 'Photo and file deleted successfully'}, status=200)
            else:
                return JsonResponse({'message': 'Photo deleted, but file not found'}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)