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
            image = 'default_profile_image.jpg',
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

    def test_new_view(self):
        self.client.force_login(self.user)
        url = reverse('item:new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'item/form.html')

        data = {
            'category' : self.category.pk,
            'created_by' : self.user.pk,
            'name': self.item.name,
            'description': self.item.description,
            'price': self.item.price,
            'image': self.item.image,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (New Item):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_edit_view(self):
        self.client.force_login(self.user)
        url = reverse('item:edit', kwargs={'primary_key': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'item/form.html')

        data = {
            'category' : self.category.pk,
            'created_by' : self.user.pk,
            'name': self.item.name,
            'description': self.item.description,
            'price': self.item.price,
            'image': self.item.image,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Item):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.item.delete()
        self.category.delete()
        self.profile.delete()
        self.user.delete()