from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from item.views import view_items, view_item_detail, create_item, update_item, delete
from item.models import Category, Item

class ItemUrlTestCase(TestCase):
    def setUp(self):
        self.test_user = self.create_test_user()
        self.test_category = self.create_test_category()
        self.test_item = self.create_test_item()

    def tearDown(self):
        self.test_item.delete()
        self.test_category.delete()
        self.test_user.delete()

    def test_index_url(self):
        url = reverse('item:items')
        self.assertEquals(resolve(url).func, view_items)
    
    def create_test_user(self):
        return User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username = 'testuser',
            email = 'emailtest',
            password = '12345'
        )

    def create_test_category(self):
        return Category.objects.create(name = 'test category')
    
    def create_test_item(self):
        return Item.objects.create(
            category = self.test_category,
            created_by = self.test_user,
            name = 'test item',
            description = 'test description',
            price = 100,
            image = 'default_profile_image.jpg'
        )

    def test_detail_url(self):
        url = reverse('item:detail', args = [self.test_item.pk])
        self.assertEquals(resolve(url).func, view_item_detail)
    
    def test_new_url(self):
        url = reverse('item:new')
        self.assertEquals(resolve(url).func, create_item)
    
    def test_edit_url(self):
        url = reverse('item:edit', args = [self.test_item.pk])
        self.assertEquals(resolve(url).func, update_item)
    
    def test_delete_url(self):
        url = reverse('item:delete', args = [self.test_item.pk])
        self.assertEquals(resolve(url).func, delete)