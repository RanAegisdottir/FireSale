from django.shortcuts import render, redirect
from create.forms.item_form import ItemCreateForm
from shop.models import ItemImage, Item


def index(request):
    return render(request, 'create/index.html')


def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(imgURL=request.POST['image'], item=item)
            item_image.save()
            request.user.save()
            return redirect('shop-index')
    else:
        form = ItemCreateForm()
    return render(request, 'create/create_item.html', {
        'form': form
    })
