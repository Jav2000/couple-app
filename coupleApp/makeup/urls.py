from django.urls import path
from . import views

app_name = 'makeup'

urlpatterns = [
    path('', views.makeup_items_page, name='makeup_items_page'),
    path('category/<str:category_name>/', views.category_items, name='category_items'),
    path('category/<str:category_name>/subcategory/<str:subcategory_name>/', views.subcategory_items, name='subcategory_items'),
    path('<int:pk>/', views.item_details_page, name='item_details_page'),
    path('new-owned-item/', views.new_owned_item, name='new_owned_item'),
    path('new-wanted-item/', views.new_wanted_item, name='new_wanted_item'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
]