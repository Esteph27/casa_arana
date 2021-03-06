from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>', views.product_info, name="product_info"),
    path('product_review/<int:product_id>', views.product_review, name="product_review"),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    # artisan profile:
    path('artisan_profile/<int:product_artisan_id>/', views.artisan_profile, name="artisan_profile"),
]
