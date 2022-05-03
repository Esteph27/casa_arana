from django.shortcuts import render


def index(request):
    """ Returns index page """

    return render(request, 'home/index.html')


def about(request):
    """ Returns about page """

    return render(request, 'home/about.html')
