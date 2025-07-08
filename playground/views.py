from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
from django.db.models import Q

def say_hello(request):
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    return render(request,'hello.html',{'name':'Aabiskar', 'products': list(queryset)})
