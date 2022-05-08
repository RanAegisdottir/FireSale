from django.shortcuts import render, get_object_or_404
from myprofile.models import UserImage
from shop.models import Offers


# Create your views here.
def index(request):
    return render(request, 'myprofile/account.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id)
    })


def edit_profile(request):
    return render(request, 'myprofile/edit_profile.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id)
    })


def my_offers(request):
    return render(request, 'myprofile/my_offers.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.all()
    })


def purchases(request):
    return render(request, 'myprofile/purchases.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id)
    })


def my_items(request):
    return render(request, 'myprofile/my_items.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id)
    })


def sold(request):
    return render(request, 'myprofile/sold.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id)
    })

