"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

import phones.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', phones.views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', phones.views.show_product, name='slugslug'),
    path('catalog?sort=name',phones.views.sort_name, name='sort_name'),
    path('catalog?sort=min_price',phones.views.sort_price_min, name='sort_min'),
    path('catalog?sort=max_price',phones.views.sort_price_max, name='sort_max')
]
