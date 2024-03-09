from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the right plural name in the admin site.
        verbose_name_plural = 'Categories'
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
PREDEFINED_CATEGORIES = [
    "Women's Clothing and Shoes",
    "Men's Clothing and Shoes",
    "Toys and Games",
    "Vehicles",
    "Furniture",
    "Electronics",
    "Properties for Rent",
    "Properties for Sale",
    "Antiques and collectibles",
    "Appliances",
    "Arts and Crafts",
    "Baby",
    "Books, Films and Music",
    "Car parts",
    "DIY and Tools",
    "Health and Beauty",
    "Home goods and decor",
    "Jewellery and watches",
    "Luggage and bags",
    "Musical Instruments",
    "Pet supplies",
    "Vehicles",
    "Not Specified"
]

@receiver(post_migrate)
def check_categories(sender, **kwargs):
    # Check if Category table is empty
    if Category.objects.count() == 0:
        # If empty, populate with predefined categories
        for category_name in PREDEFINED_CATEGORIES:
            Category.objects.create(name=category_name)
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='item_images', default='default_item_image.png', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name


