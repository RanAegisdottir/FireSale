from django.shortcuts import render, redirect
from checkout.models import Payments, Order
from checkout.forms.checkout_form import CheckoutForm
from myprofile.models import UserImage, Users
from shop.models import Offers


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
                               companyname=company_name, country=country, street=street, zip=zip, city=city, phone=phone, confirmed=False)
            payment.save()
            offer_id = request.GET.get('offer-id', '')
            offer = Offers.objects.get(id=offer_id)
            order = Order(offerID=offer, payID=payment, confirmed=False)
            order.save()
            return render(request, 'checkout/confirm.html', {
                'order': Order.objects.get(id=order.id),
                'Image': UserImage.objects.get(user_id=request.user.id)})

    else:
        form = CheckoutForm()
        offer_id = request.GET.get('offer-id', '')
    return render(request, 'checkout/checkout_payment.html', {
        'form': form,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'offer_id': offer_id})


def confirm(request, payment_id):
    return render(request, 'checkout/confirm.html', {
        'payment': Payments.objects.get(id=payment_id),
        'Image': UserImage.objects.get(user_id=request.user.id)})



def save(request):
    payment_id = request.GET.get('payment-id', '')
    payment = Payments.objects.get(id=payment_id)
    order_id = request.GET.get('order-id', '')
    order = Order.objects.get(id=order_id)
    payment.confirmed = True
    payment.save()
    order.confirmed = True
    order.save()
    return render(request, 'checkout/save.html')


def review(request):
    return

