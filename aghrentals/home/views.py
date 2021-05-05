from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def homePage(request):
    return render(request, "home.html")


@login_required(login_url="/accounts/login/")
def newPage(request):
    return render(request, "newpage.html")


def sample(request):
    return HttpResponse(str(request))
