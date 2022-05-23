from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.order_checkout, name="order_checkout"),
    path('checkout_success/<order_id>', views.checkout_success, name="checkout_success"),
    path('wh/', webhook, name="webhook"),
]
