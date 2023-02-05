from distutils.sysconfig import customize_compiler
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from . import models

# Create your views here.
def product_page(request):
    search_product = ""
    if request.GET.get("search_product"):
        search_product = request.GET.get("search_product")
    product = models.Product.objects.filter(
        Q(name__icontains=search_product) | Q(description__icontains=search_product)
    )
    context = {"product": product, "search_product": search_product}
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
