from django.forms import ModelForm, widgets
from checkout.models import Payments

class CheckoutForm(ModelForm):
    class Meta:
        model = Payments
        exclude = ['id', 'userID', 'confirmed']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'companyname': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_num': widgets.TextInput(attrs={'class': 'form-control'}),
            'exdate': widgets.TextInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }
