from django.db import models
from myprofile.models import Users


class Conditions(models.Model):
    status = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    seller = models.ForeignKey(Users, on_delete=models.CASCADE)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE)
    available = models.BooleanField()


class ItemImage(models.Model):
    imgURL = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Offers(models.Model):
    buyer = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()
    accepted = models.BooleanField()