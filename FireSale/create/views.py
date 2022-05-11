from django.shortcuts import render, redirect
from create.forms.item_form import ItemCreateForm
from myprofile.models import UserImage, Users
from shop.models import ItemImage, Item


def index(request):
    return render(request, 'create/index.html')


def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            condition = form.cleaned_data.get("condition")
            priceidea = form.cleaned_data.get("priceidea")
            item = Item(name=name, description=description,
                        condition=condition, priceidea=priceidea, seller=request.user)
            item.save()
            first_item_image = ItemImage(imgURL=request.POST['first_image'], item=item)
            first_item_image.save()
            second_item_image = ItemImage(imgURL=request.POST['second_image'], item=item)
            third_item_image = ItemImage(imgURL=request.POST['third_image'], item=item)
            fourth_item_image = ItemImage(imgURL=request.POST['fourth_image'], item=item)
            if second_item_image != '':
                second_item_image.save()
            if third_item_image != '':
                third_item_image.save()
            if fourth_item_image != '':
                fourth_item_image.save()

            return redirect('shop-index')
    else:
        form = ItemCreateForm()
    return render(request, 'create/create_item.html', {
        'form': form,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })
