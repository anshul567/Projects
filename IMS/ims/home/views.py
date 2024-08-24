from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
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
    
    
@csrf_exempt
def product_list_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def product_detalil_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)

    except product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)
    elif request.method == 'GET':
        serializer = ProductSerializers(product)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializers(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    