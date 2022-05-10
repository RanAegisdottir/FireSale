from django.forms import ModelForm, widgets
from django import forms
from myprofile.models import Users


class EditProfileForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Users
        exclude = ['user', 'rating']
        widgets = {
            'fullname': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.TextInput(attrs={'class': 'form-control'})
        }