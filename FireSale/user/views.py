from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import render, redirect
from myprofile.models import UserImage, Users


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        errors = form.errors
        if form.is_valid():
            user = form.save()
            user_img = UserImage(user_image='https://www.nicepng.com/png/detail/73-730154_open-default-profile-picture-png.png', user=user)
            user_img.save()
            user_info = Users(bio="", rating=0, user=user)
            user_info.save()
            return redirect('login')
        else:
            return render(request, 'user/register.html', {'form': form})
    return render(request, 'user/register.html', {
        'form': UserCreationForm(),
        'UserInfo': Users.objects.get(user_id=request.user.id)
    })
