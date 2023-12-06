from django.test import TestCase
from django.contrib.auth.models import User
from item.models import Category, Item

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def tearDown(self):
        self.category.delete()

class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(category=self.category, created_by=self.user, name='Test Item', price=50)

    def tearDown(self):
        self.item.delete()
        self.category.delete()
        self.user.delete()
