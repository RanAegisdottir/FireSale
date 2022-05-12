from django.forms import ModelForm, widgets
from shop.models import Offers


# form for offer, only take the offer amount
class OfferForm(ModelForm):
    class Meta:
        model = Offers
        exclude = ['id', 'accepted', 'outbid', 'buyer', 'item']
        widgets = {
            'Your offer': widgets.NumberInput(attrs={'class': 'form-control'})
        }