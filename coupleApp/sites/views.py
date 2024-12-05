from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Site, Photo
from .forms import SiteForm

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


def add_photos(request, pk):
    site = get_object_or_404(Site, pk=pk)

    if request.method == 'POST':
        images = request.FILES.getlist('images')  # Obtén la lista de archivos cargados
        response_data = []
        
        for file in images:
            photo = Photo(image=file, site=site)  # Crea una nueva instancia de Photo
            photo.save()  # Guarda la foto en la base de datos
            response_data.append({
                'photo_url': photo.image.url,
                'success': True,
            })
        
        return JsonResponse(response_data, safe=False)

    else:
        return render(request, 'add_photos.html', {})
