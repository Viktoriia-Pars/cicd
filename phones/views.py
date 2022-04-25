from django.shortcuts import render
from .models import *


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones':Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)

def sort_price_min(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.order_by('price')}
    return render(request, template, context)

def sort_price_max(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.order_by('-price')}
    return render(request, template, context)

def sort_name(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.order_by('name')}
    return render(request, template, context)

