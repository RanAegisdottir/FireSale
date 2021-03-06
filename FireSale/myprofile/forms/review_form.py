from django.forms import ModelForm, widgets
from checkout.models import Reviews


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ['id', 'offer', 'seller']
        widgets ={
            'rating': widgets.Select(attrs={'class': 'form-control'})
        }
