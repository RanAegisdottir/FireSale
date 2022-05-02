from django.db import models


class Users(models.Model):
    userID: models.IntegerField()
    name: models.CharField(max_length=255)
    email: models.CharField(max_length=255)
    username: models.CharField(max_length=255)
    password: models.CharField(max_length=255)
    bio: models.CharField(max_length=300)
    rating: models.IntegerField()


class UserImage(models.Model):
    user_image: models.CharField(max_length=9999)
    user: models.ForeignKey(Users, on_delete=models.CASCADE)


class Stars(models.Model):
    star_img: models.CharField(max_length=9999)
    # á þetta að vera int
    star_num: models.IntegerField()
    user: models.ForeignKey(Users, on_delete=models.CASCADE)


class Reviews(models.Model):
    reviewID: models.IntegerField()
    text: models.CharField(max_length=300)
    rating: models.IntegerField()
    #Order: models.ForeignKey(Order, on_delete=models.CASCADE)


class Order(models.Model):
    orderId: models.IntegerField()
    #offerID: models.ForeignKey(Offers, on_delete=models.CASCADE)
    #payID: models.ForeignKey(Payments, on_delete=models.CASCADE)


class Offers(models.Model):
    offerID: models.IntegerField()
    buyerID: models.ForeignKey(Users, on_delete=models.CASCADE)
    #itemID: models.ForeignKey(Item, on_delete=models.CASCADE)
    amount: models.IntegerField()
    accepted: models.BooleanField()


class Payments(models.Model):
    payID: models.IntegerField()
    userID: models.ForeignKey(Users, on_delete=models.CASCADE)
    card_name: models.CharField(max_length=255)
    card_num: models.IntegerField()
    exdate: models.DateField()
    CVC: models.IntegerField()
    companyname: models.CharField(max_length=255)
    #countryID: models.ForeignKey(Country, on_delete=models.CASCADE)
    street: models.CharField(max_length=255)
    zip: models.IntegerField()
    city: models.CharField(max_length=255)
    phone: models.IntegerField()


