"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from django.conf.urls import include


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls), 
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blog-single/', views.single_blog, name = "blog-single"),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('project-detail/', views.project_detail, name = 'project-detail'),
    path('service-detail/', views.service_detail, name = 'service-detail'),
    path('services/', views.services, name = 'service'),
    path('shop-cart/', views.shop_cart, name = 'shop-cart'),
    path('shop-single/', views.single_shop, name = 'shop-single'),
    path('page-shop/', views.shop_page, name = 'page-shop'),

]
