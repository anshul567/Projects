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
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()
router.register('products', ProductViewSet, basename='api_products')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pform/', ProductCreateView.as_view(), name='pform'),
    path('plist/', ProductListView.as_view(), name='plist'),
    path('pupdate/<pk>/', ProductUpdateView.as_view(), name='pupdate'),
    path('pdelete/<pk>/', ProductDeleteView.as_view(), name='pdelete'),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),


]
