from django.db import models
from django.db.models import JSONField


# Create your models here.
class Customer(models.Model):
    company = models.CharField(max_length=80, default="")
    sex = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=30, default="")
    tel = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    contact = JSONField(default=dict)
    is_won = models.BooleanField(default=False)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
