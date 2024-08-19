from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
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