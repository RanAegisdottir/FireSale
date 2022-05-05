from django.forms import ModelForm, widgets
from shop.models import Item
from django import forms


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'available', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'priceidea': widgets.NumberInput(attrs={'class': 'form-control'})
            # 'available': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
