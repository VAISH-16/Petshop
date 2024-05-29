from django.test import TestCase
from .models import Product
# Create your tests here.
def add(a,b):
    return 0

class ProductTest(TestCase):
    def setUp(self):
        self.product=Product.productManager.create(product_name="testProduct",
                                      product_description="description for test product",
                                      product_brand="superpet",
                                      product_price=500,
                                      product_picture="abc.jpeg"
                                      )
    def test_create_product(self):
        product=Product.productManager.get(id=self.product.id)
        self.assertEqual(self.product,product)

    def test_all_users(self):
        products=Product.productManager.all()
        self.assertTrue(len(products)>0)
    
    def test_add(self):
        self.assertEqual(add(5,5),10)
    
        