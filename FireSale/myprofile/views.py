from django.shortcuts import render
from django.urls import reverse

from myprofile.models import UserImage
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'myprofile/account.html', {'Users': request.user, 'Image': UserImage.objects.get(user_id=request.user.id)})


# def anchor(url_name, section_id):
#     return reverse(url_name) + '#' + section_id