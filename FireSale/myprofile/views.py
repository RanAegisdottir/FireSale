from django.shortcuts import render, get_object_or_404, redirect
from myprofile.forms.edit_profile_form import EditProfileForm
from myprofile.forms.review_form import ReviewForm
from myprofile.models import UserImage, Users
from notification.models import Notifications
from shop.models import Offers, ItemImage, Item
from checkout.models import Order, Reviews



#Main profile site where you can see your fullname, bio, image and reviews
def index(request):
    user_reviews = Reviews.objects.filter(seller_id=request.user.id)
    return render(request, 'myprofile/account.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Reviews': user_reviews
    })

#Edit profile site
def edit_profile(request):
    instance = get_object_or_404(Users, user=request.user)
    user = Users.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get("fullname")
            bio = form.cleaned_data.get("bio")
            user.fullname = fullname
            user.bio = bio
            user.save()
            user_img = UserImage.objects.get(user=request.user)
            user_img.user_image = request.POST['image']
            user_img.save()
            return redirect('myprofile-index')
    else:
        form = EditProfileForm(instance=instance)
        form.fields['image'].initial = UserImage.objects.filter(user=request.user).first()
    return render(request, 'myprofile/edit_profile.html', {
        'form': form,
        'id': id,
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })

#my offers site
def my_offers(request):
    return render(request, 'myprofile/my_offers.html', {
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'Available_Offers': Offers.objects.filter(buyer_id=request.user.id, item__available=True),
        'Declined_Offers': Offers.objects.filter(buyer_id=request.user.id, item__available=False, accepted=False),
        'ItemImage': ItemImage.objects.all(),
        'Orders': Order.objects.all(),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })

#purchases site
def purchases(request):
    return render(request, 'myprofile/purchases.html', {
        'purchased_by': Order.objects.filter(payID__userID=request.user.id),
        # 'same_user_in_offers': Offers.objects.filter(buyer=purchased_by, Item=item),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.filter(buyer_id=request.user.id, accepted=True, item__available=False)
    })

#my items site
def my_items(request):
    return render(request, 'myprofile/my_items.html', {
        'my_items_products': Item.objects.filter(seller=request.user.id, available=True),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Offers': Offers.objects.all()
    })

#sold items site
def sold(request):
    return render(request, 'myprofile/sold.html', {
        'sold_products': Item.objects.filter(seller=request.user.id, available=False),
        'Users': request.user,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })

#When you accept an offer a notification sends to all the users that offered in the item
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

#review site
def review(request):
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            offer_id = request.GET.get('offer-id', '')
            offer = Offers.objects.get(id=offer_id)
            item_review = Reviews(offer_id=offer.id, rating=rating, seller_id=offer.item.seller.id)
            item_review.save()
            reviews = Reviews.objects.filter(seller_id=offer.item.seller.id)

        #calculating the average rating
            total = 0
            count = 0
            for x in reviews:
                total += x.rating.star_num
                count += 1

            avg_rating = total // count
            user = Users.objects.get(user_id=offer.item.seller.id)
            user.rating = avg_rating
            user.save()

            return redirect('myprofile-index')
    else:
        form = ReviewForm()
        offer_id = request.GET.get('offer-id', '')
    return render(request, 'myprofile/review.html', {
        'form': form,
        'offer_id': offer_id,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })