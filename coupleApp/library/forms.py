from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'isbn', 'genre', 'publish_date', 'pages', 'cover_image']