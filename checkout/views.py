from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def order_checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There are no items in your bag at the moment.")
        return redirect(reverse('products'))
    

    order_from = OrderForm()
    template = 'checkout/order_checkout.html'
    context = {
        'order_form' = order_from
    }

    return render(request, template, context)