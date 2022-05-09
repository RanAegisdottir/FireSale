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
            company_name = form.cleaned_data.get('company name')
            card_name = form.cleaned_data.get('card name')
            card_num = form.cleaned_data.get('card number')
            exdate = form.cleaned_data.get('exdate')
            cvc = form.cleaned_data.get('CVC')

            payment = Payment(street=street, zip=zip, city=city, phone=phone, country=country, company_name=company_name,
                              card_name=card_name, card_num=card_num, exdate=exdate, cvc=cvc, userID=request.user)
            payment.save()
            return redirect('myprofile-index')

    else:
        form = CheckoutForm()
    return render(request, 'checkout/checkout_payment.html')

