from django.shortcuts import render, redirect, get_object_or_404
from checkout.models import Payments, Order
from checkout.forms.checkout_form import CheckoutForm
from myprofile.models import UserImage, Users
from shop.models import Offers, Item

#View for checkout
def index(request):
    return render(request, 'checkout/index.html')


def checkout_payment(request):
    offer_id = request.GET.get('offer-id', '')

    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        # Submission is valid, continue
        if form.is_valid():
            #  CVC is invalid  (custom validation)
            cvc = form.cleaned_data.get('CVC')
            if not cvc.isnumeric():
                form.add_error('CVC', 'Only numbers allowed in CVC')
                return render(request, 'checkout/checkout_payment.html', {
                    'form': form,
                    'Image': UserImage.objects.get(user_id=request.user.id),
                    'UserInfo': Users.objects.get(user_id=request.user.id),
                    'offer_id': offer_id})
            #  Card_num is invalid  (custom validation)
            card_num = form.cleaned_data.get('card_num')
            if not card_num.isnumeric():
                form.add_error('card_num', 'Only numbers allowed in Card number')
                return render(request, 'checkout/checkout_payment.html', {
                    'form': form,
                    'Image': UserImage.objects.get(user_id=request.user.id),
                    'UserInfo': Users.objects.get(user_id=request.user.id),
                    'offer_id': offer_id})

            street = form.cleaned_data.get('street')
            zip = form.cleaned_data.get('zip')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            country = form.cleaned_data.get('country')
            company_name = form.cleaned_data.get('companyname')
            card_name = form.cleaned_data.get('card_name')
            exdate = form.cleaned_data.get('exdate')

            payment = Payments(userID=request.user, card_name=card_name, card_num=card_num, exdate=exdate, CVC=cvc,
                               companyname=company_name, country=country, street=street, zip=zip, city=city,
                               phone=phone, confirmed=False)
            payment.save()

            offer = Offers.objects.get(id=offer_id)
            order = Order(offerID=offer, payID=payment, confirmed=False)
            order.save()
            return render(request, 'checkout/confirm.html', {
                'order': Order.objects.get(id=order.id),
                'Image': UserImage.objects.get(user_id=request.user.id),
                'UserInfo': Users.objects.get(user_id=request.user.id)})

        # submission is not valid, send form back with errors
        return render(request, 'checkout/checkout_payment.html', {
            'form': form,
            'Image': UserImage.objects.get(user_id=request.user.id),
            'UserInfo': Users.objects.get(user_id=request.user.id),
            'offer_id': offer_id})

    #If user goes back to change his information this code prepopulates the form so he doesnt
    #have to put all the information back in.
    if request.GET.get('pay-id', '') != '':
        order_id = request.GET.get('pay-id', '')
        order = Order.objects.get(payID=order_id)
        payment = order.payID
        instance = get_object_or_404(Payments, id=payment.id)
        form = CheckoutForm(instance=instance)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout_payment.html', {
        'form': form,
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id),
        'offer_id': offer_id})


#Show all the checkout detail and order detail
def confirm(request, payment_id):
    return render(request, 'checkout/confirm.html', {
        'payment': Payments.objects.get(id=payment_id),
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)})


def save(request):
    payment_id = request.GET.get('payment-id', '')
    payment = Payments.objects.get(id=payment_id)
    order_id = request.GET.get('order-id', '')
    order = Order.objects.get(id=order_id)
    payment.confirmed = True
    payment.save()
    order.confirmed = True
    order.save()
    item = Item.objects.get(id=order.offerID.item.id)
    item.available = False
    item.save()
    return render(request, 'checkout/save.html', {
        'Image': UserImage.objects.get(user_id=request.user.id),
        'UserInfo': Users.objects.get(user_id=request.user.id)})
