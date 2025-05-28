from django.urls import path
from . import views

app_name = 'skincare'

urlpatterns = [
    path('', views.skincare_products_page, name='skincare_products_page'),
    path('category/<str:category_name>/', views.category_products, name='category_products'),
    path('<int:pk>/', views.skincare_product_details_page, name='skincare_product_details_page'),
    path('new-owned-skincare-product/', views.new_owned_skincare_product, name='new_owned_skincare_product'),
    path('new-wanted-skincare-product/', views.new_wanted_skincare_product, name='new_wanted_skincare_product'),
    path('<int:pk>/edit/', views.edit_skincare_product, name='edit_skincare_product'),
    path('<int:pk>/delete/', views.delete_skincare_product, name='delete_skincare_product'),
]