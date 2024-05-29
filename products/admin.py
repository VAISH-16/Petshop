from django.contrib import admin
from .models import Product,Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','product_price','category']

# Registering product model on the admin panel
# admin.site.register(Product,ProductAdmin)  Method 1
# @admin.register(Product) Method 2

# ---------------------------
# Registering Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

admin.site.register(Category,CategoryAdmin)


