from django.shortcuts import render


def view_shopping_bag(request):
    """ Renders the shopping bag page and contents """

    return render(request, 'shopping_bag/shopping_bag.html')
