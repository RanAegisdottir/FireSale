from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shop-index"),
    path('<int:id>', views.get_item_by_id, name='item-details'),
    path('invalid_offer/<int:id>', views.invalid_offer, name='invalid-offer')
]