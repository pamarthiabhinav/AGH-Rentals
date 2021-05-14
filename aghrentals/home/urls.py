from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('new/', views.newPage, name="newPage"),
    path('issuesSend/', views.issuesSend, name="issuesSend"),
]
