from django.shortcuts import render, get_object_or_404
from myprofile.models import UserImage


# Create your views here.
def index(request):
    return render(request, 'myprofile/account.html', {
        'Users': request.user,
        'Image': UserImage.objects.all()
    })


def edit_profile(request):
    return render(request, 'myprofile/edit_profile.html', {
        'Users': request.user,
        'Image': UserImage.objects.all()
    })


def my_offers(request):
    return render(request, 'myprofile/my_offers.html', {
        'Users': request.user
    })


def purchases(request):
    return render(request, 'myprofile/purchases.html', {
        'Users': request.user
    })


def my_items(request):
    return render(request, 'myprofile/my_items.html', {
        'Users': request.user
    })


def sold(request):
    return render(request, 'myprofile/sold.html', {
        'Users': request.user
    })


