from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def order_checkout(request):
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/order_checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KjjqeGaYG4N8lqVCgdSemyW9gPGI5Jgzik3zMeQlnowMn4mGkf85BJhTClZJVrW7tusX3C2WhspltnhwdU4DP1800xYVwQ2t1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)