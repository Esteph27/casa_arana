from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_id>', views.order_history, name='order_history'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('add_or_remove_item_from_wishlist/<product_id>', views.add_or_remove_item_from_wishlist, name='add_or_remove_item_from_wishlist'),
]