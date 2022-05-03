from django.shortcuts import render, get_object_or_404
from shop.models import Item

# Create your views here.
def index(request):
    context = {'products': Item.objects.all().order_by('name')}
    return render(request, 'shop/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'shop/item_details.html', {
        'Item': get_object_or_404(Item, pk=id)
    })