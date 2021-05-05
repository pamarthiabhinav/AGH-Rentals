from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<center><h1>Welome To AGH Rentals</h1></center>")
