from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('', views.checkout_payment, name="checkout-payment"),
    path('confirm', views.confirm, name="confirm"),
    path('', views.index, name="checkout-index"),
]