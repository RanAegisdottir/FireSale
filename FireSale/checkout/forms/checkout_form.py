from django.forms import ModelForm, widgets
from django import forms
from checkout.models import Payments
from django_countries.widgets import CountrySelectWidget


class ExDateInput(forms.DateInput):
    input_type = 'date'


class CheckoutForm(ModelForm):
    class Meta:
        model = Payments
        exclude = ['id', 'userID', 'confirmed']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street-name...'}),
            'housenumber': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Housenumber...'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip...'}),
            'city': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City...'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number...'}),
            'country': CountrySelectWidget(attrs={'class': 'form-country-input'}),
            'fullname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname...'}),
            'companyname': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name...'}),
            'card_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cardholder Name...'}),
            'card_num': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card-number...'}),
            'exdate': ExDateInput(attrs={'class': 'form-control'}),
            'CVC': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC...'})
        }
