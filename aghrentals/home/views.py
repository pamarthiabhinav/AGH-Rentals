from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import issue
from django.contrib import messages

# Create your views here.


def homePage(request):
    return render(request, "home.html")


@login_required(login_url="/accounts/login/")
def newPage(request):
    return render(request, "newpage.html")


def issuesSend(request):
    if request.method == "POST":
        first_name = last_name = email = ""
        if request.user.is_authenticated:
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
        else:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")
        myissue = issue(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            message=message
        )
        myissue.save()
        messages.success(
            request, "Your Issue Has Been Successfully Registered")
    return redirect('homePage')


def sample(request):
    return HttpResponse(str(request))
