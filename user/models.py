from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_no = models.CharField(max_length=80, unique=True, blank=True, null=True)
    company = models.CharField(max_length=80, default="")
    sex = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=30, default="")
    tel = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=150, unique=True, blank=True, null=True)
    contact = models.CharField(max_length=100, default="")
    is_won = models.BooleanField(default=False)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
