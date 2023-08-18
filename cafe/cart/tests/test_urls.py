from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import *

class TestUrls(SimpleTestCase):
    def test_cart_url_is_resolved(self):

        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, CartView)



    