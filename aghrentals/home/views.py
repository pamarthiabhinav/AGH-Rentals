from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import issue
from products.models import Company
from django.contrib import messages

# Create your views here.


def homePage(request):
    bikes = Company.objects.filter(category='bike')
    cars = Company.objects.filter(category='car')
    cameras = Company.objects.filter(category='camera')
    myDict = {'bike': bikes, 'cars': cars, 'cameras': cameras}
    # return render(request, "home.html", company=myDict)
    return render(request, "home.html", myDict)


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
    return redirect('/#support')


def sample(request):
    return HttpResponse(str(request))


@login_required(login_url="/accounts/login/")
def newPage(request):
    return render(request, "order_placed.html")
