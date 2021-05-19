from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('check/<int:id>', views.check_order, name="check_order"),
    path('place/<int:id>', views.place_order, name="place_order"),
]
