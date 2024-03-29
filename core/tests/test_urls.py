from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import home, index, signin, signup, logout

class CoreTestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func, home) 

    def test_index_url(self):
        url = reverse('core:index')
        self.assertEquals(resolve(url).func, index)

    def test_signin_url(self):
        url = reverse('core:signin')
        self.assertEquals(resolve(url).func, signin)

    def test_signup_url(self):
        url = reverse('core:signup')
        self.assertEquals(resolve(url).func, signup)
    
    def test_logout_url(self):
        url = reverse('core:logout')
        self.assertEquals(resolve(url).func, logout)
