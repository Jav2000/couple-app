from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]