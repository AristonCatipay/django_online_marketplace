from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

