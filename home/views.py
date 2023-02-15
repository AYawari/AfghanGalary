from distutils.sysconfig import customize_compiler
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

# Create your views here.
def product_page(request):
    category = ''
    
    if request.GET.get('women'):
        category = request.GET.get('women')
    elif request.GET.get('men'):
        category = request.GET.get('men')     
    elif request.GET.get('watch'):
        category = request.GET.get('watch')     
    elif request.GET.get('shoes'):
        category = request.GET.get('shoes')     
    elif request.GET.get('bag'):
        category = request.GET.get('bag')     

    product = models.Product.objects.filter(
        Q(product_type__icontains=category)
    )
    
    
    page = request.GET.get('page')
    paginator = Paginator(product, 8)
    
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        product = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages()
        product = paginator.page(page)              
    context = {"product": product,'paginator':paginator, 'category':category}
    return render(request, "home/index.html", context)

def search(request):
    search_product = ""
    if request.GET.get("search_product"):
        search_product = request.GET.get("search_product")    
    products = models.Product.objects.filter(
        Q(name__icontains=search_product)
    )
    context = {
        "search_product": search_product,
        "product": products
    }
    return render(request, 'home/index.html', context)

def product_detail(request, pk):

    product = models.Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "home/product_detail.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = models.OrderItem.objects.get_or_create()
        items = order.orderitem_set.all()
    else:
        items = []
    context = {"items": items}

    return render(request, "home/checkout.html", context)
