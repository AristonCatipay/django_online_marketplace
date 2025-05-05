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

    def test_user_relationship(self):
        expected_user = self.profile.user
        self.assertEqual(expected_user.username, 'testuser')

    def test_image_content(self):
        expected_image = f'{self.profile.image}'
        self.assertEqual(expected_image, 'media/default_profile_image.jpg')

    def test_location_content(self):
        expected_location = f'{self.profile.location}'
        self.assertEqual(expected_location, 'Some Location')