from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('one_page', views.one_page)
]