from django.db import models
from myprofile.models import Users
from django.conf import settings


class Conditions(models.Model):
    status = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.status


class Item(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE, default=None)
    available = models.BooleanField(default=True)
    priceidea = models.FloatField(default=None)
    heighestoffer = models.FloatField(default=None)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    imgURL = models.CharField(max_length=9999, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)


class Offers(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(default=None)
    accepted = models.BooleanField(default=None)
    outbid = models.BooleanField(default=False)