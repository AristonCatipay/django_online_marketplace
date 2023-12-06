from django.test import TestCase
from django.contrib.auth.models import User
from item.models import Category, Item

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def tearDown(self):
        self.category.delete()
