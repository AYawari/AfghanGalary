from distutils.command.upload import upload
import email
from itertools import product
from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class Customer
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
#class Product
class Product(models.Model):
    product_size_choices = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Larg', 'Larg'),
        ('Xlarg', 'Xlarg'),
        ('FreeSize', 'FreeSize'),
    ]
    product_type_choices = [
        ('Men', 'Men'),
        ('Women', 'Womem'),
        ('Shose', 'Shose'),
        ('Watch', 'Watch'),
        ('Bag', 'Bag'),
    ]
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    size = models.CharField(max_length=10, choices=product_size_choices, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    product_type = models.CharField(max_length=10, choices=product_type_choices, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url        
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)    
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    Order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    home_address = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=200)
    date_of_address = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.home_address
        
        
    
    
    
        
    
    
    
    
    