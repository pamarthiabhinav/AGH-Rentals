from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import UserProfile
from order.models import order
from django.contrib import messages
# Create your views here.


def acountsHome(request):
    return redirect('profilePage')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        uname = request.POST["username"]
        email = request.POST["email"]
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile(username=request.user).save()
            return redirect('homePage')
        else:
            pass
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        uname = request.POST["username"]
        if User.objects.filter(username=uname).exists():
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect('homePage')
            else:
                messages.error(request, 'username or password is Incorrect')
        else:
            messages.error(
                request, f'Account Does Not Exists For This Username: { uname }')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        try:
            del request.session['userBike']
            del request.session['userCar']
            del request.session['userCamera']
            del request.session['totalBike']
            del request.session['totalCar']
            del request.session['totalCamera']
        except:
            pass
        logout(request)
    return redirect('homePage')


@login_required(login_url='/accounts/login')
def profilePage(request):
    totBikeCnt = len(order.objects.filter(prod__category='bike'))
    totCarCnt = len(order.objects.filter(prod__category='car'))
    totCameraCnt = len(order.objects.filter(prod__category='camera'))
    userBikeCnt = len(order.objects.filter(
        prod__category='bike', user=request.user))
    userCarCnt = len(order.objects.filter(
        prod__category='car', user=request.user))
    userCameraCnt = len(order.objects.filter(
        prod__category='camera', user=request.user))
    request.session['userBike'] = userBikeCnt
    request.session['userCar'] = userCarCnt
    request.session['userCamera'] = userCameraCnt
    request.session['totalBike'] = totBikeCnt
    request.session['totalCar'] = totCarCnt
    request.session['totalCamera'] = totCameraCnt

    userProf = UserProfile.objects.filter(username=request.user)
    orders = order.objects.filter(user=request.user)
    myDict = {"userProf": userProf, "order": orders}
    return render(request, 'profile.html', myDict)
