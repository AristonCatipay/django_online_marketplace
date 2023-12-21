from django.db import models
from django.contrib.auth.models import User

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


