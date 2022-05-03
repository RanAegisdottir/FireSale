from django.db import models
from myprofile.models import Users


class Conditions(models.Model):
    status = models.CharField(max_length=255, default=None)


class Item(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    seller = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE, default=None)
    available = models.BooleanField(default=None)
    priceidea = models.FloatField(default=None)


class ItemImage(models.Model):
    imgURL = models.CharField(max_length=9999, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)


class Offers(models.Model):
    buyer = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(default=None)
    accepted = models.BooleanField(default=None)
    