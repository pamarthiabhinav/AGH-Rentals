from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bikeHome, name="bikeHome"),
    path('<str:company>/', views.bikeHome, name="parameterBikeHome"),
]
