from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from myprofile.models import UserImage
from shop.models import Item

# Create your views here.
def index(request):
    if 'search-filter' in request.GET:
        search_filter = request.GET['search-filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'seller': x.seller,
            'condition': x.condition,
            'available': x.available,
            'priceidea': x.priceidea,
            'image': x.itemimage_set.first().imgURL
        } for x in Item.objects.filter(name_icontains=search_filter)]
        return JsonResponse({'data': products})

    context = {'products': Item.objects.all().order_by('name'),
               'Image': UserImage.objects.get(user_id=request.user.id)}
    return render(request, 'shop/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'shop/item_details.html', {
        'Item': get_object_or_404(Item, pk=id),
        'Image': UserImage.objects.get(user_id=request.user.id)
    })