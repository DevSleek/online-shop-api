from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'description']
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
