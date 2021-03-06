from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    category model
    """
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(null=True, blank=True, max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Product information
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    color = models.CharField(max_length=254, null=True, blank=True)
    dimensions = models.CharField(max_length=200, null=True, blank=True)
    composition = models.CharField(max_length=300, null=True, blank=True)
    features = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)

    artisan = models.ForeignKey(
        'Artisan', null=True, blank=False, on_delete=models.SET_NULL, related_name="products")

    def __str__(self):
        return self.name


class Artisan(models.Model):
    """
    Artisan information
    """

    name = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=200)
    story = models.TextField(max_length=1000, blank=True)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


RATING_CHOICES = [ 
    (1, '1 - Very Bad'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
]

class Reviews(models.Model):
    """
    Product review model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    text = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.user.username
