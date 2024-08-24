from .models import Product
from rest_framework import serializers


class ProductSerializers(serializers.Serializer):
    product_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    sku = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    supplier = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        product = Product(**validated_data)
        product.product_id=instance.product_id
        product.save()
        return product

