from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages 

from products.models import Product


def view_shopping_bag(request):
    """ Renders the shopping bag page and contents """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add item to bag and quantity to shopping bag"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else: 
        bag[item_id] = quantity
        messages.success(request, f'{product.name} added to your bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_qty(request, item_id):
    """ Adjust the quantity of sepecific product"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
    
    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})

      
        if not bag[item_id]:
            bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)