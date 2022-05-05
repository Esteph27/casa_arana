from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ 
    Returns all products page, includes search queries and filtering 
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)
