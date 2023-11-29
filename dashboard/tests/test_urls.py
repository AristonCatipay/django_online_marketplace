from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import index

class DashboardUrlTestCase(SimpleTestCase):
    def test_index_url(self):
        url = reverse('dashboard:index')
        self.assertEquals(resolve(url).func, index)