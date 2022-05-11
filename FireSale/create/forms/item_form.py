from django.forms import ModelForm, widgets
from shop.models import Item
from django import forms


class ItemCreateForm(ModelForm):
    first_image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    third_image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fourth_image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'available', 'seller', 'heighestoffer']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'priceidea': widgets.NumberInput(attrs={'class': 'form-control'})
        }
