from django.contrib import admin
from .models import Orders,OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model=OrderItem


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=['order_id','user','first_name','phoneno','created_at','paid']
    inlines=[OrderItemInline]




