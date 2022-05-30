from django.contrib import admin
from .models import Wishlist, WishListItem

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(WishListItem)

