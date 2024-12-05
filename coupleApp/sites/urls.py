from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'sites'  # Namespace para la aplicación 'sites'

urlpatterns = [
    path('', views.sites_page, name='sites_page'), # URL for the main sites page
    path('<int:pk>/', views.site_details_page, name='site_details_page'),  # URL for the site details
    path('sites/mapa-datos/', views.sites_geojson, name='sites_geojson'), # URL for JSON sites data
    path('new-site/', views.new_site, name='new_site'),
    path('<int:pk>/add-photos/', views.add_photos, name='add_photos'),  # Ruta para agregar fotos
]

if settings.DEBUG:  # Solo para el entorno de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)