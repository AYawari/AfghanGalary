from distutils.sysconfig import customize_compiler
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models

# Create your views here.
def product_page(request):
    search_product = ""
    if request.GET.get("search_product"):
        search_product = request.GET.get("search_product")
    product = models.Product.objects.filter(
        Q(name__icontains=search_product) | Q(description__icontains=search_product)
    )
    if product.product_type:
        product_type = models.Product.objects.filter(product_type)
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
            
    # leftindex = (int(page)-3)
    # if leftindex<1:
    #     leftindex = 1
    
    # rightindex = (int(page)+2)        
    # if rightindex > paginator.num_pages:
    #     rightindex = paginator.num_pages + 1
    # custom_range = range(leftindex, rightindex)               
    context = {"product": product, "search_product": search_product, 'paginator':paginator}
    return render(request, "home/index.html", context)


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
