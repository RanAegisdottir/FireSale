from django.shortcuts import render
from create.forms.item_form import ItemCreateForm


# Create your views here.


def index(request):
    return render(request, 'create/index.html')


def create_item(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ItemCreateForm()
    return render(request, 'create_item.html', {
        'form': form
    })
