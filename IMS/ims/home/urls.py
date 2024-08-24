"""
URL configuration for ims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pform/', ProductCreateView.as_view(), name='pform'),
    path('plist/', ProductListView.as_view(), name='plist'),
    path('pupdate/<pk>/', ProductUpdateView.as_view(), name='pupdate'),
    path('pdelete/<pk>/', ProductDeleteView.as_view(), name='pdelete'),
    path('api/plist/', APIProductListView.as_view(), name='api_plist' ),
    path('api/plist/<pk>/', APIProductDetailView.as_view(), name='api_plist_pk' )
]
