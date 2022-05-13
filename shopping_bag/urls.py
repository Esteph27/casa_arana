from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name="view_shopping_bag"),
    path('add/<item_id>/', views.add_to_bag, name="add_to_bag"),
    path('adjust/<item_id>/', views.adjust_bag_qty, name="adjust_bag_qty"),
    path('remove/<item_id>/', views.remove_from_bag, name="remove_from_bag"),
]
