from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Item
from .forms import ItemForm

# Create your views here.
def makeup_items_page(request):
    items = Item.objects.all().order_by('-updated_at', 'owned')
    return render(request, 'makeup_items_page.html', {'items': items})

def category_items(request, category_name):
    items = Item.objects.filter(category__iexact=category_name)  # Filtra por categoría (case-insensitive)
    return render(request, 'makeup_category_items.html', {'items': items, 'category_name': category_name})

def subcategory_items(request, category_name, subcategory_name):
    items = Item.objects.filter(category__iexact=category_name, subcategory__iexact=subcategory_name)
    return render(request, 'makeup_subcategory_items.html', {
        'items': items,
        'category_name': category_name,
        'subcategory_name': subcategory_name,
    })

def item_details_page(request, pk):
    item = get_object_or_404(Item, pk=pk)
    redirect_url = request.GET.get('redirect_to', None)
    print(redirect_url)

    return render(request, 'makeup_item_details_page.html', {'item': item, 'redirect_url': redirect_url})

def new_owned_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owned = True 
            item.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ItemForm()

    return render(request, 'new_owned_item.html', {'form': form})

def new_wanted_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owned = False
            item.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ItemForm()

    return render(request, 'new_wanted_item.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('makeup:item_details_page', pk=pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_makeup_item.html', {'form': form, 'item': item})

def delete_item(request, pk):
    trip = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('makeup:makeup_items_page')
    return render(request, 'delete_confirmation.html', {'trip': trip})