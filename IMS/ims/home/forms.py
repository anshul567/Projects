from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['product_id']
        labels = {
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g. S123FG', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 19.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'e.g. 100', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g. ABC Corp', 'class': 'form-control'}),  
        }