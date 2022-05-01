from django.urls import path
from . import views

urlpatterns = [
    # htp://localhost:8000/shop
    path('', views.index, name="shop-index"),
]