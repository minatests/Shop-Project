from django.test import TestCase, Client
from django.urls import reverse
from menu.models import Category, Product



class TestMenuView(TestCase):

    def setUp(self):
        self.client= Client()
        self.menu_url = reverse('menu')

    def test_menu_view_GET(self):
        response = self.client.get(self.menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')


class TestSearchProducts(TestCase):
    def setUp(self):
        self.client= Client() 
        self.search_product_url = reverse('search_products')
        self.category = Category.objects.create( name = "category 1", photo = 'test.png')
        self.product1 = Product.objects.create( name = "product 1", price = 20.12 , category_menu = self.category,photo = 'product.png', status = 'active', )
        self.product2 = Product.objects.create( name = "product 2", price = 10.12 , category_menu = self.category,photo = 'product.png', status = 'active', )

    def test_search_product_GET(self):
        response = self.client.get(self.search_product_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/search_results.html')
        

    def test_search_product_with_query_context(self):
        query1 = "product 1"
        response = self.client.get(self.search_product_url, {"query": query1 })
        
        self.assertContains(response, query1)
        self.assertIn(self.product1, response.context["results"])
        self.assertNotIn(self.product2, response.context["results"])


    def test_search_product_with_empty_query_context(self):
        query1 = ""
        response = self.client.get(self.search_product_url, {"query": query1 })
        self.assertEqual(len(response.context["results"]), 0)



class TestProductPopup(TestCase):
    def setUp(self):
        self.client= Client() 
        self.category = Category.objects.create( name = "category 1", photo = 'test.png')
        self.product = Product.objects.create( name = "product 1", price = 10.12 , category_menu = self.category,photo = 'product.png', status = 'active', )
        self.product_popup_url = reverse('product_popup', kwargs={'product_id': 1})

    def test_product_popup_GET(self):
        response = self.client.get(self.product_popup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/product_detail.html')

    def test_product_popup_context(self):
        response = self.client.get(self.product_popup_url)
        self.assertEqual(response.context['product'], self.product)