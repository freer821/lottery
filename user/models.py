from django.db import models
from django.db.models import JSONField


# Create your models here.
class Customer(models.Model):
    type = models.CharField(max_length=80, default="") # new customer or registered
    customer_no = models.CharField(max_length=80, unique=True, blank=True, null=True)
    company = models.CharField(max_length=80, default="")
    sex = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    company_extra = models.CharField(max_length=200, default="")
    addr = models.CharField(max_length=250, default="")
    addr_extra = models.CharField(max_length=250, default="")
    city = models.CharField(max_length=100, default="")
    postcode = models.CharField(max_length=20, default="")
    country = models.CharField(max_length=30, default="")
    tel = models.CharField(max_length=50, default="")
    fax = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    bill_email = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=150, default="")
    tax_id = models.CharField(max_length=100, default="")
    ust_id = models.CharField(max_length=100, default="")
    bank = models.CharField(max_length=100, default="")
    iban = models.CharField(max_length=30, default="")
    bic = models.CharField(max_length=10, default="")
    contact = JSONField(default=dict)
    is_won = models.BooleanField(default=False)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
