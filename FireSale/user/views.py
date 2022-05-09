from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from myprofile.models import UserImage, Users


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_img = UserImage(user_image='https://www.nicepng.com/png/detail/73-730154_open-default-profile-picture-png.png', user=user)
            user_img.save()
            user_info = Users(bio="", rating=0, user=user)
            user_info.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })
