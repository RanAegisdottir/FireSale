from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('', views.index, name="checkout-index"),
]