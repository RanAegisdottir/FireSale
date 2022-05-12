from django.db import models
from myprofile.models import Users
from django.conf import settings


# get the conditions of the items
class Conditions(models.Model):
    status = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.status


# model for the items
class Item(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE, default=None)
    available = models.BooleanField(default=True)
    priceidea = models.FloatField(default=None)
    # we know that highest offer is typed wrong, we just did not fix it
    heighestoffer = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


# model for the items images
class ItemImage(models.Model):
    imgURL = models.CharField(max_length=50000, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)


# model for the offers for the items
class Offers(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    amount = models.FloatField(default=None)
    accepted = models.BooleanField(default=False)
    outbid = models.BooleanField(default=False)