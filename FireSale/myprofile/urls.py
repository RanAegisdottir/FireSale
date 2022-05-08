from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/myprofile/
    path('', views.index, name="myprofile-index"),
    path('editProfile/', views.edit_profile, name='edit_profile'),
    path('offers/', views.my_offers, name='my_offers'),
    path('purchases/', views.purchases, name='purchases'),
    path('items/', views.my_items, name='my_items'),
    path('sold/', views.sold, name='sold')
]


