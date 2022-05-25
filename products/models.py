from django.db import models

# Create your models here.

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
    Product info model
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    color = models.CharField(max_length=254, null=True, blank=True)
    dimensions_and_composition = models.TextField()
    features = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
