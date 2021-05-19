from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.carHome, name="carHome"),
    path('<str:company>/', views.carHome, name="parameterCarHome"),
]
