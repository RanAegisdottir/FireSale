from django.shortcuts import render, get_object_or_404, redirect
from myprofile.models import UserImage, Users
from notification.models import Notifications
from shop.models import Offers, ItemImage, Item
from checkout.models import Order, Payments




# Create your views here.
def index(request):
    return render(request, 'myprofile/account.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })


def edit_profile(request):
    return render(request, 'myprofile/edit_profile.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })


def my_offers(request):
    return render(request, 'myprofile/my_offers.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.filter(buyer_id=request.user.id),
        'ItemImage': ItemImage.objects.all(),
        'Orders': Order.objects.all(),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })


def purchases(request):
    return render(request, 'myprofile/purchases.html', {
        'purchased_by': Order.objects.filter(payID__userID=request.user.id),
        # 'same_user_in_offers': Offers.objects.filter(buyer=purchased_by, Item=item),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.filter(buyer_id=request.user.id, accepted=True)
    })


def my_items(request):
    return render(request, 'myprofile/my_items.html', {
        'my_items_products': Item.objects.filter(seller=request.user.id, available=True),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.all()
    })


def sold(request):
    return render(request, 'myprofile/sold.html', {
        'sold_products': Item.objects.filter(seller=request.user.id, available=False),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })


def accept(request):
    offer_id = request.GET.get('offer-id', '')
    offer = Offers.objects.get(id=offer_id)
    offer.accepted = True
    offer.save()
    offers = Offers.objects.filter(item_id=offer.item_id)
    for x in offers:
        notification = Notifications(offer_id=x.id, seller_id=request.user.id)
        notification.save()
    return redirect('my_items')
