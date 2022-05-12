from django.shortcuts import render, redirect


def view_shopping_bag(request):
    """ Renders the shopping bag page and contents """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add item to bag and quantity to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else: 
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
