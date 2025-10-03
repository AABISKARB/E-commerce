from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem
from django.db.models import Q

def say_hello(request):
    queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct())
    return render(request,'hello.html',{'name':'Aabiskar', 'products': list(queryset)}) 