from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bio = models.CharField(max_length=300)
    rating = models.IntegerField()


class UserImage(models.Model):
    user_image = models.CharField(max_length=9999)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)







