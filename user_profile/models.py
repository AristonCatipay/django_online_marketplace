from django.db import models
from django.contrib.auth.models import User
from address.models import Region, Province, City_Municipality, Barangay

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=OTHERS)
    location = models.CharField(max_length=100, blank=True)
    barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
    city_municipality = models.ForeignKey(City_Municipality, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

