from django.conf import settings
from django.db import models


class Users(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    bio = models.CharField(max_length=300, default=None)
    rating = models.IntegerField(default=None)

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user_image = models.CharField(max_length=9999, default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user_image







