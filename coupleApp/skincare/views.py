from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import SkincareProduct
from .forms import SkincareProductForm

# Create your views here.
def skincare_products_page(request):
    skincare_products = SkincareProduct.objects.all().order_by('-updated_at', 'owned')
    return render(request, 'skincare_products_page.html', {'skincare_products': skincare_products})

def category_products(request, category_name):
    skincare_products = SkincareProduct.objects.filter(category__iexact=category_name)  # Filtra por categoría (case-insensitive)
    return render(request, 'skincare_category_products.html', {'skincare_products': skincare_products, 'category_name': category_name})

def skincare_product_details_page(request, pk):
    skincare_product = get_object_or_404(SkincareProduct, pk=pk)
    redirect_url = request.GET.get('redirect_to', None)
    print(redirect_url)

    return render(request, 'skincare_product_details_page.html', {'skincare_product': skincare_product, 'redirect_url': redirect_url})

def new_owned_skincare_product(request):
    if request.method == 'POST':
        form = SkincareProductForm(request.POST, request.FILES)
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
        form = SkincareProductForm()

    return render(request, 'new_owned_skincare_product.html', {'form': form})

def new_wanted_skincare_product(request):
    if request.method == 'POST':
        form = SkincareProductForm(request.POST)
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
        form = SkincareProductForm()

    return render(request, 'new_wanted_skincare_product.html', {'form': form})

def edit_skincare_product(request, pk):
    skincare_product = get_object_or_404(SkincareProduct, pk=pk)
    if request.method == 'POST':
        form = SkincareProductForm(request.POST, instance=skincare_product)
        if form.is_valid():
            form.save()
            return redirect('makeup:item_details_page', pk=pk)
    else:
        form = SkincareProductForm(instance=skincare_product)
    return render(request, 'edit_skincare_product.html', {'form': form, 'skincare_product': skincare_product})

def delete_skincare_product(request, pk):
    skincare_product = get_object_or_404(SkincareProduct, pk=pk)
    if request.method == 'POST':
        skincare_product.delete()
        return redirect('skincare:skincare_products_page')
    return render(request, 'delete_confirmation.html', {'skincare_product': skincare_product})