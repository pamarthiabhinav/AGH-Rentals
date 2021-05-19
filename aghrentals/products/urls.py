from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_details, name="product_details"),
    path('place/<int:id>', views.place_order, name="place_order"),
    path('<int:id>/', views.product_details, name="product_details"),
]
