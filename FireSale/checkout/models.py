from django.conf import settings
from django.db import models
from myprofile.models import Users
from shop.models import Offers
from django_countries.fields import CountryField


class Payments(models.Model):
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    card_name = models.CharField(max_length=255, default=None)
    card_num = models.BigIntegerField(default=None)
    exdate = models.DateField(default=None)
    CVC = models.IntegerField(default=None)
    companyname = models.CharField(max_length=255, default=None, blank=True)
    country = CountryField(blank_label='(select country)', default=None)
    street = models.CharField(max_length=255, default=None)
    zip = models.IntegerField(default=None)
    city = models.CharField(max_length=255, default=None)
    phone = models.IntegerField(default=None)
    confirmed = models.BooleanField(default=False)


class Order(models.Model):
    offerID = models.ForeignKey(Offers, on_delete=models.CASCADE, default="")
    payID = models.ForeignKey(Payments, on_delete=models.CASCADE, default="")
    confirmed = models.BooleanField(default=False)


class Stars(models.Model):
    star_num = models.IntegerField(default=0)

    def __str__(self):
        return str(self.star_num)


class Reviews(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    rating = models.ForeignKey(Stars, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default="")


