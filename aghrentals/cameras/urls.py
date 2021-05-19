from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cameraHome, name="cameraHome"),
    path('<str:company>/', views.cameraHome, name="parameterCameraHome"),
]
