from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'trips'  # Namespace para la aplicación 'trips'

urlpatterns = [
    path('', views.trips_page, name='trips_page'),
    path('<int:pk>/', views.trip_details_page, name='trip_details_page'),
    path('mapa-datos/', views.trips_geojson, name='trips_geojson'),
    path('new-trip/', views.new_trip, name='new_trip'),
    path('<int:pk>/edit/', views.edit_trip, name='edit_trip'),
    path('<int:pk>/delete/', views.delete_trip, name='delete_trip'),
    path('<int:pk>/add-photos/', views.add_trip_photos, name='add_trip_photos'),
    path('delete-photo/<int:photo_id>/', views.delete_trip_photo, name='delete_trip_photo'),
    path('get-google-maps-key/', views.get_google_maps_key, name='get_google_maps_key'),
]

if settings.DEBUG:  # Solo para el entorno de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)