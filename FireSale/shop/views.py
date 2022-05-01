from django.shortcuts import render

products = [
    {'name': 'shoes', 'price': 30},
    {'name': 'car', 'price': 200}
]

# Create your views here.
def index(request):
    return render(request, 'shop/index.html', context={ 'products': products })
