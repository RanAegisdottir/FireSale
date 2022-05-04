from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/create
    path('', views.create_item, name="create_item"),
    path('', views.index, name="create-index"),
]
