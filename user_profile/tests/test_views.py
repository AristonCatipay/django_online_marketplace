from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('profile:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'profile/index.html')
        
    def tearDown(self):
        # Cleanup after each test
        self.user.delete()