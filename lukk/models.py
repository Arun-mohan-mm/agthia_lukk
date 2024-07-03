from django.db import models


class Customer_details(models.Model):
    name = models.CharField(max_length=200, null=True)
    civil_id = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    receipt_number = models.CharField(max_length=200, null=True)
    voucher_number = models.CharField(max_length=200, null=True)

