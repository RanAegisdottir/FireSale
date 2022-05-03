from django.db import models
from myprofile.models import Users
from shop.models import Offers
from django_countries.fields import CountryField


class Country(models.Model):
    pass
    #country = CountryField(blank_label='(select country)')


class Payments(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=255)
    card_num = models.IntegerField()
    exdate = models.DateField()
    CVC = models.IntegerField()
    companyname = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    zip = models.IntegerField()
    city = models.CharField(max_length=255)
    phone = models.IntegerField()


class Order(models.Model):
    pass
    #offerID = models.ForeignKey(Offers, on_delete=models.CASCADE)
    #payID = models.ForeignKey(Payments, on_delete=models.CASCADE)


class Reviews(models.Model):
    text = models.CharField(max_length=300)
    rating = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Stars(models.Model):
    star_img = models.CharField(max_length=9999)
    # á þetta að vera int
    star_num = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
