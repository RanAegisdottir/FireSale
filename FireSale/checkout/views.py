from django.shortcuts import render
from myprofile.models import UserImage

# Create your views here.
def index(request):
    contex = {'Image': UserImage.objects.get(user_id=request.user.id)}
    return render(request, 'checkout/index.html', contex)
