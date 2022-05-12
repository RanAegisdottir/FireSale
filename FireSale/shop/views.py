from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from myprofile.models import UserImage, Users
from shop.models import Item, Offers
from shop.forms.offer_form import OfferForm

# Create your views here.
def index(request):
    # search filter
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'priceidea': x.priceidea,
            'heighestoffer': x.heighestoffer,
            'image': x.itemimage_set.first().imgURL
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    # filter by price or name
    if 'order' in request.GET:
        order = request.GET['order']
        if order == 'order-alpha':
            order_string = 'name';
        if order == 'price-high':
            order_string = '-heighestoffer';
        if order == 'price-low':
            order_string = 'heighestoffer';
        products = [{
            'id': x.id,
            'name': x.name,
            'priceidea': x.priceidea,
            'heighestoffer': x.heighestoffer,
            'image': x.itemimage_set.first().imgURL
        } for x in Item.objects.order_by(order_string)]
        return JsonResponse({'data': products})

    # show all products
    context = {'products': Item.objects.all(),
               'Image': UserImage.objects.get(user_id=request.user.id),
               'UserInfo': Users.objects.get(user_id=request.user.id)}
    return render(request, 'shop/index.html', context)

# show similar items, get item by id and place offer form
def get_item_by_id(request, id):
    # similar items
    products = Item.objects.filter(~Q(pk=id))[:3]
    # if there is a offer post request
    if request.method == 'POST':
        form = OfferForm(data=request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            offer = Offers(buyer=request.user, item=Item.objects.get(pk=id), amount=amount)
            item = Item.objects.get(pk=id)
            if amount < item.heighestoffer:
                return redirect('invalid-offer', id=item.id)
            offer.save()

            item_offers = Offers.objects.filter(item=item)
            for x in item_offers:
                if x.amount > item.heighestoffer:
                    item.heighestoffer = x.amount
                    item.save()
                else:
                    x.outbid = True
                    x.save()

            return render(request, 'shop/item_details.html', {
                'products': products,
                'Item': get_object_or_404(Item, pk=id),
                'UserInfo': Users.objects.get(user_id=request.user.id),
                'Image': UserImage.objects.get(user_id=request.user.id),
                'form': OfferForm()
            })
        else:
            form = OfferForm()
            return render(request, 'shop/item_details.html', {
                'products': products,
                'Item': get_object_or_404(Item, pk=id),
                'UserInfo': Users.objects.get(user_id=request.user.id),
                'Image': UserImage.objects.get(user_id=request.user.id),
                'form': form
            })

    return render(request, 'shop/item_details.html', {
        'products': products,
        'Item': get_object_or_404(Item, pk=id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'Image': UserImage.objects.get(user_id=request.user.id),
        'form': OfferForm()
    })

def invalid_offer(request, id):
    context = {'product': Item.objects.filter(pk=id).first()}
    return render(request, 'shop/offer_low.html', context)

