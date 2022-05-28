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
    wishlist = profile.wishlist.all()

    template = 'user_profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        'wishlist': wishlist,
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
def add_to_wishlist(request, product_id):
    """
    Add a product to wish list
    """

    redirect_url = request.POST.get('redirect_url') 
    
    # get product from product page 
    product = get_object_or_404(Product, product_id=product_id)
    

    # create wishlist if one does not exsist
    wishlist = WishList.objects.get_or_create(user=request.user)
    # Add product to the wishlist
    wishlist.products.add(product)
    messages.info(request, 'Added to your wish list')

    return redirect(redirect_url)