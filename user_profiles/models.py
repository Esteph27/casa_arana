from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from products.models import Product


class UserProfile(models.Model):
    """
    Model to store a user's default delivery information and order history
    """
    # user info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_contact_number = models.CharField(max_length=20, null=True, blank=True)
    
    # delivery address
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Wishlist(models.Model):
    """
    Model to store products in a user's wish list
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='WishListItem')

    def __str__(self):
        return f'wishlist ({self.user})'


class WishListItem(models.Model):
    """
    Through model allowing user to add products to their wishlist
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.product.name
