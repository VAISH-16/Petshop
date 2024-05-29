from django.db import models
from autoslug import AutoSlugField

# Create your models here.
    
# -------------------------------------------------------
#    Custom Manager (Product)
# --------------------------------------------------------

class CustomProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model)
        # return super().get_queryset().order_by('product_name')
    
    def royalCanin(self):
        return super().get_queryset().filter(product_brand="Royal Canin")
    
    def drools(self):
        return super().get_queryset().filter(product_brand="drools")
    
    
# -------------------------------------------------------
#    Custom QuerySet (Product)
# --------------------------------------------------------

class ProductQuerySet(models.QuerySet):

    def range(self,start_price,end_price):
        return self.filter(product_price__range=(start_price,end_price))
    
    def search(self,keyword):
        return self.filter(product_name__icontains=keyword)
    
# =====================================================================
#   Category Models
# =====================================================================

class Category(models.Model):
    category_name=models.CharField(max_length=50,blank=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name



# -----------------------------------------------------------------

# (objects)

class Product(models.Model):
    product_name=models.CharField(max_length=70,default="product name")
    product_description=models.TextField(default="Description")
    product_price=models.PositiveIntegerField(default=0)
    product_brand=models.CharField(max_length=50,default="superpet")
    product_picture=models.ImageField(upload_to="products/",null=True)
    # ForeignKey(one to Many)(One category many peoducts
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)

    # Changing manager name(Product.productManger.all())
    productManager=models.Manager()
    cm=CustomProductManager()


    def __str__(self):
        return self.product_name
