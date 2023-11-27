from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import home, index, signin, signup, logout

class CoreTestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func, home) 
        

    
