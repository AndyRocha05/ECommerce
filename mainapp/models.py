from django.db import models
import re

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=63)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=127)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    ted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    name = models.CharField(max_length=127)
    img = models.ImageField()
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Admin(models.Model):
    email = models.CharField(max_length=127)
    password = models.CharField(max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer_fname = models.CharField(max_length=127)
    customer_lname = models.CharField(max_length=127)

    s_address = models.CharField(max_length=127)
    s_city = models.CharField(max_length=127)
    s_state = models.CharField(max_length=2)
    s_zipcode = models.IntegerField()

    b_address = models.CharField(max_length=127)
    b_city = models.CharField(max_length=127)
    b_state = models.CharField(max_length=2)
    b_zipcode = models.IntegerField()

    order_status = models.CharField(max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductToOrder(models.Model):
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    order = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)

    qty = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)