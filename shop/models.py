from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(verbose_name="Product Name", max_length= 200)
    price= models.FloatField(verbose_name="Price")
    discount_price= models.FloatField(verbose_name="Discounted Price")
    category= models.CharField(verbose_name="Category",max_length=200)
    description= models.TextField(verbose_name="Product Description")
    image= models.CharField(verbose_name="Product Image",max_length= 300) 

class Orders(models.Model):
    items= models.CharField(max_length=1000)
    email= models.CharField(max_length=500)
    address= models.CharField(max_length=1000)
    city= models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    zipcode= models.CharField(max_length=100)
    name= models.CharField(max_length=200)
    