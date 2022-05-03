from django.shortcuts import render
from myprofile.models import Users

# Create your views here.
def index(request):
    return render(request, 'myprofile/index.html', {'Users': Users.objects.all()})
