"""
URL configuration for App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App2.views import *

urlpatterns = [
                  path('', index, name="index"),
                  path('admin/', admin.site.urls),
                  path('products/', user_login, name='user_login'),
                  path('user_logout/', user_logout, name='user_logout'),
                  path('register/', register, name='register'),
                  path('products_list/', product_list, name='product_list'),
                  path('product/<int:product_id>/', product_details, name='product_details'),
                  path('new/', new, name="new"),
                  path('checkout/<int:product_id>/', checkout, name='checkout'),
                  path('checkout_confirmation/', checkout_confirmation, name='checkout_confirmation'),
                  path('create_product/', create_product, name='create_product'),
                  path('all_products/', product_list, name='all_products'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
