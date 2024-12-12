from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import Trip
from gallery.models import Photo
from .forms import TripForm

import os

# Create your views here.
def trips_page(request):
    trips = Trip.objects.all()
    return render(request, 'trips_page.html', {'trips': trips})

def trip_details_page(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'trip_details_page.html', {'trip': trip})

def trips_geojson(request):
    trips = Trip.objects.all()
    features = []

    for trip in trips:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [trip.longitude, trip.latitude]
            },
            "properties": {
                "destiny": trip.destiny,
                "description": trip.description,
                "pk": trip.pk
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return JsonResponse(geojson)

def get_google_maps_key(request):
    return JsonResponse({'apiKey': settings.GOOGLE_MAPS_API_KEY})

def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo sitio en la base de datos
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = TripForm()

    return render(request, 'new_trip.html', {'form': form})

def edit_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trips:trip_details_page', pk=pk)
    else:
        form = TripForm(instance=trip)
    return render(request, 'edit_trip.html', {'form': form, 'trip': trip})

def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trips:trips_page')
    return render(request, 'delete_confirmation.html', {'trip': trip})

def add_trip_photos(request, pk):
    print("Hola")
    trip = get_object_or_404(Trip, pk=pk)

    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'success': False, 'message': 'The file is not getting to the server.'}, status=400)
        
        image = request.FILES['image']
        response_data = []

        try:
            if image.size > 5 * 1024 * 1024:  # Limitar tamaño del archivo a 5MB
                raise ValidationError("El archivo es demasiado grande.")
            
            photo = Photo(image=image, trip=trip)  # Crea una nueva instancia de Photo
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
        return render(request, 'add_trip_photos.html', {'trip': trip})

def delete_trip_photo(request, photo_id):
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