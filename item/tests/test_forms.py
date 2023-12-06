from django.test import TestCase
from item.forms import NewItemForm, EditItemForm
from item.models import Item, Category
from django.contrib.auth.models import User

class TestForms(TestCase):
    def setUp(self):
        self.test_category = Category.objects.create(name='Test Category')
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        self.test_category.delete()
        self.test_user.delete()