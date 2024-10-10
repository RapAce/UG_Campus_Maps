from django.db import models
from category.models import Category


class Venue(models.Model):
    name=models.CharField(max_length=120)
    category= models.ForeignKey(Category, default=1,on_delete=models.CASCADE)
    address=models.CharField(max_length=120)
    latitude=models.CharField(max_length=120)
    longitude=models.CharField(max_length=120)
    phonenumber=models.CharField(max_length=120,blank=True)
    openinghours=models.TextField(blank=True)
    type=models.CharField(max_length=120,blank=True)
    imageurl=models.CharField(max_length=1000,blank=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    indoormap=models.URLField(blank=True)

    def __str__(self):
        return self.name


