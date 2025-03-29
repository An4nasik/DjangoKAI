# DjangoKAIProject/urls.py
from django.urls import path
from BaseApp import views

urlpatterns = [
    path('', views.star_list, name='star_list'),
    path('add/', views.add_star, name='add_star'),
]