from django.shortcuts import render

from myprofile.models import UserImage
from notification.models import Notifications
from shop.models import Offers


def index(request):
    return render(request, 'notification/notifications.html',
                  {'User': request.user,
                   'Notification': Notifications.objects.all(),
                   'Image': UserImage.objects.get(user_id=request.user.id)})
