from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

