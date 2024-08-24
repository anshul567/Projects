from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.http import Http404
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'home/pform.html'
    
    def get_success_url(self):
        return reverse_lazy('plist')

class ProductListView(ListView):
    model = Product
    template_name = 'home/plist.html'
    context_object_name = 'products'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'home/pform.html'
    
    def get_success_url(self):
        return reverse_lazy('plist')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'home/pcdelete.html'
    
    def get_success_url(self):
        return reverse_lazy('plist')


class APIProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class APIProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# class APIProductListView(APIView):

#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data) 
    
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class APIProductDetailView(APIView):

#     def get_product(self, pk):
#         try:
#              return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
    
#     def put(self, request, pk):
#         product = self.get_product(pk)
#         serializer = ProductSerializer(product, data=serializer.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, pk):
#         product = self.get_product(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         product = self.get_product(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def product_list_view(request):
#     if request.method == 'GET':
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['PUT','GET','DELETE'])
# def product_detalil_view(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)

#     except product.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=204)
#     elif request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    