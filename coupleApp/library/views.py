from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Book
from .forms import BookForm

def library_page(request):
    books = Book.objects.all()
    return render(request, 'library_page.html', {'books': books})

def book_details_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_details_page.html', {'book': book})

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = BookForm()

    return render(request, 'new_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:book_details_page', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, pk):
    trip = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('library:library_page')
    return render(request, 'delete_confirmation.html', {'trip': trip})