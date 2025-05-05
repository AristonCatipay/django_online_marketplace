from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import view_user_items

class DashboardUrlTestCase(SimpleTestCase):
    def test_index_url(self):
        url = reverse('dashboard:index')
        self.assertEquals(resolve(url).func, view_user_items)