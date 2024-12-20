from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library_page, name='library_page'),
    path('<int:pk>/', views.book_details_page, name='book_details_page'),
    path('new-book/', views.new_book, name='new_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]