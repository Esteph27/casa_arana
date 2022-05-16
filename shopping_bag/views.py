from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages 

from products.models import Product


def view_shopping_bag(request):
    """ Renders the shopping bag page and contents """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add item to bag and quantity to shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'{product.name} added to your bag')
        messages.success(request, f'You now have {bag[item_id]} of the {product.name} in your bag')
    else: 
        bag[item_id] = quantity
        messages.success(request, f'{product.name} added to your bag')
        
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_qty(request, item_id):
    """ Adjust the quantity of sepecific product"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} quantity updated to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if not bag[item_id]:
            bag.pop(item_id)
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
