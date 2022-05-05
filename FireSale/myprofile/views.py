from django.shortcuts import render
from myprofile.models import UserImage
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'myprofile/account.html', {'Users': request.user, 'Image': UserImage.objects.all()})


def get_profile_info(request):
    return render(request.user)