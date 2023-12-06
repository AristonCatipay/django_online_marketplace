from django.test import TestCase
from django.contrib.auth.models import User
from item.models import Category, Item

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def tearDown(self):
        self.category.delete()

    def test_name_content(self):
        expected_name = f'{self.category.name}'
        self.assertEqual(expected_name, 'Test Category')

class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(category=self.category, created_by=self.user, name='Test Item', price=50)

    def tearDown(self):
        self.item.delete()
        self.category.delete()
        self.user.delete()

    def test_name_content(self):
        expected_name = f'{self.item.name}'
        self.assertEqual(expected_name, 'Test Item')

    def test_price_content(self):
        self.assertEqual(self.item.price, 50)

    def test_is_sold_default(self):
        self.assertFalse(self.item.is_sold)

    def test_category_relationship(self):
        category = self.item.category
        self.assertEqual(category.name, 'Test Category')

    def test_user_relationship(self):
        user = self.item.created_by
        self.assertEqual(user.username, 'testuser')
