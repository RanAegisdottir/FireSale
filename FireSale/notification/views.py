from django.shortcuts import render
from notification.models import Notifications
from shop.models import Offers


def index(request):
    return render(request, 'notification/notifications.html',
                  {'User': request.user,
                   'Notification': Notifications.objects.all()})
