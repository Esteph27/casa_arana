from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User


from .models import Product, Category, Artisan, Reviews
from user_profiles.models import Wishlist
from .forms import ProductForm, ReviewsForm


def all_products(request):
    """
    Returns all products, includes search queries and filtering
    """

    products = Product.objects.all()
    catergory = Category.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Looks like you didn't enter anything, please try again")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search': query,
        'catergory': catergory,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/all_products.html', context)


def product_info(request, product_id):
    """
    Shows product information for a single product
    """

    artisan = Product.artisan
    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.filter(product=product)

    context = {
        'product': product,
        'artisan': artisan,
        'reviews': reviews,
    }

    return render(request, 'products/product_info.html', context)


def product_review(request, product_id):
    """
    Handles products reviews
    """

    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            messages.success(request, f'Thank you for your review.')
            return redirect(reverse('product_info', args=[product_id]))
    else:
        form = ReviewsForm()


    context = {
        'form': form,
        'product': product,
    }

    return render(request,  'products/product_review.html', context)



def artisan_profile(request, product_artisan_id):
    """
    A view to render Artisan profile of a selected Artisan
    """

    artisan = get_object_or_404(Artisan, pk=product_artisan_id)
    products = Product.objects.filter(artisan=product_artisan_id)

    template = 'products/artisan_profile.html'

    context = {
        'artisan': artisan,
        'products': products,
    }

    return render(request, template, context)



# ---------------------- admin
@login_required
def add_product(request):
    """
    Add a product to the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Unauthorized action. Only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid and try again.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Unauthorized action. Only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid and try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Unauthorized action. Only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('products'))
