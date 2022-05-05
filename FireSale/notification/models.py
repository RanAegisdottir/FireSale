from django.conf import settings
from django.db import models
from shop.models import Offers


class Notifications(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, default=None)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
