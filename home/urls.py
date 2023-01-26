import imp
from django.urls import path
from . import views
urlpatterns = [
    path('home', views.product_page, name='home'),
    path('detail/<int:pk>', views.product_detail, name='detail'),
    path('checkout', views.checkout, name='checkout')
]
