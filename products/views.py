from django.shortcuts import render
from .models import Product

# Create your views here.
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def create_products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render (request, 'products-form.html', {'form': form})