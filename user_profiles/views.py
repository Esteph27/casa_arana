from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm


from checkout.models import Order


@login_required
def profile(request):
    """
    Display user's profile account.
    User can update default delivery info, view order histroy
    and wishlist items
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid and try again')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'user_profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


def order_history(request, order_id):
    """
    get user's order histroy by order number
    """

    order = get_object_or_404(Order, order_id=order_id)

    messages.info(request, (
        f'You are viewing a past order confirmation for order #{order_id}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def view_wishlist(request):
    """
    A view to render a user's wish list
    """
    
    wishlist = Wishlist.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'user_profiles/wishlist.html'

    context = {
        'wishlist': wishlist,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def add_or_remove_item_from_wishlist(request, product_id):
    """
    Handles adding and removing items from wish list when user clicks on heart icon
    """

    user = request.user
    product_id = request.POST.get('product_id')
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        wishlist = Wishlist.objects.filter(user=user)
        if product in wishlist.prodducts.all():
            wishlist.products.remove(product)
            messages.info(request, (
                f'{product_id} removed from your wishlist'
            ))
        else:
            wishlist.products.add(product)
            messages.info(request, (
                f'{product_id} added from your wishlist.'))
    
    return redirect(reverse('product_info'))
