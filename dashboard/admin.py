from django.contrib import admin
from .models import Order, Product
from django.contrib.auth.models import Group
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.unregister(Group)
admin.site.site_header = 'Inventory Dashboard'

