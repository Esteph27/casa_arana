from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_checkout, name="order_checkout"),
]
