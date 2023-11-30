from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item, Category
from user_profile.models import Profile

class ItemViewTestCase(TestCase):
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

        self.category = Category.objects.create(
            name = 'test category'
        )
        
        self.item = Item.objects.create(
            category = self.category,
            created_by = self.user,
            name = 'test item',
            description = 'test description',
            price = 100,
            image = 'test image',
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('item:items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'item/items.html')
    
    def test_detail_view(self):
        self.client.force_login(self.user)
        url = reverse('item:detail', kwargs={'primary_key': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'item/detail.html')

    def tearDown(self):
        self.user.delete()