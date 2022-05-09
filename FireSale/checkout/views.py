from django.shortcuts import render, redirect
from checkout.models import Payments
from checkout.forms.checkout_form import CheckoutForm


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')


def checkout_payment(request):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            street = form.cleaned_data.get('street')
            zip = form.cleaned_data.get('zip')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            country = form.cleaned_data.get('country')
            company_name = form.cleaned_data.get('companyname')
            card_name = form.cleaned_data.get('card_name')
            card_num = form.cleaned_data.get('card_num')
            exdate = form.cleaned_data.get('exdate')
            cvc = form.cleaned_data.get('CVC')

            payment = Payments(userID=request.user, card_name=card_name, card_num=card_num, exdate=exdate, CVC=cvc,
                               companyname=company_name, country=country, street=street, zip=zip, city=city, phone=phone)
            payment.save()
            return redirect('myprofile-index')

    else:
        form = CheckoutForm()
    return render(request, 'checkout/checkout_payment.html', {'form': form})

