from django.test import TestCase
from django.contrib.auth.models import User
from user_profile.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.profile = Profile.objects.create(
            user = self.user,
            image = 'media/default_profile_image.jpg',
            location = 'Some Location',
        )

    def tearDown(self):
        self.user.delete()
        self.profile.delete()