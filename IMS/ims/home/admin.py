from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]

admin.site.register(Product, ProductAdmin)