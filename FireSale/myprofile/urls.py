from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/myprofile
    path('', views.index, name="myprofile-index"),
]