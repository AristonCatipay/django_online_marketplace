from django.test import SimpleTestCase
from django.urls import reverse, resolve
from item.views import items

class ItemUrlTestCase(SimpleTestCase):
    def test_index_url(self):
        url = reverse('item:items')
        self.assertEquals(resolve(url).func, items)