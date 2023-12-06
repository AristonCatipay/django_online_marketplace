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

    def test_new_item_form_valid(self):
        form = NewItemForm(data={
            'category': self.test_category.id,
            'name': 'Test Item',
            'description': 'Test description',
            'price': 100,
            # Add other required fields or mock the required data here
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())

    def test_edit_item_form_valid(self):
        item = Item.objects.create(
            category=self.test_category,
            created_by=self.test_user,
            name='Existing Item',
            description='Old Description',
            price=50
        )
        form = EditItemForm(instance=item, data={
            'name': 'Updated Name',
            'description': 'Updated Description',
            'price': 75,
            # Add other required fields or mock the required data here
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())