from django.db import models
from myprofile.models import Users
from shop.models import Offers
from django_countries.fields import CountryField


class Country(models.Model):
    country = CountryField(blank_label='(select country)', default=None)


class Payments(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    card_name = models.CharField(max_length=255, default=None)
    card_num = models.IntegerField(default=None)
    exdate = models.DateField(default=None)
    CVC = models.IntegerField(default=None)
    companyname = models.CharField(max_length=255, default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    street = models.CharField(max_length=255, default=None)
    zip = models.IntegerField(default=None)
    city = models.CharField(max_length=255, default=None)
    phone = models.IntegerField(default=None)


class Order(models.Model):
    offerID = models.ForeignKey(Offers, on_delete=models.CASCADE, default="")
    payID = models.ForeignKey(Payments, on_delete=models.CASCADE, default="")


class Reviews(models.Model):
    text = models.CharField(max_length=300, default="")
    rating = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default="")


class Stars(models.Model):
    star_img = models.CharField(max_length=9999, default="")
    # á þetta að vera int
    star_num = models.IntegerField(default=0)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default="")