from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    return HttpResponse("<center><h1>Welome To AGH Rentals</h1></center>")


def login_cancelled(request):
    messages.success(request, 'Error In The Authentication!')
    return redirect('login')

def error_404(request, exception):  
    return HttpResponse("Page Not Found")
