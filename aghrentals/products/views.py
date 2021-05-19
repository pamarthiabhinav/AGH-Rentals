from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import product

# Create your views here.


def product_details(request, id=None):
    if id:
        products = product.objects.filter(id=id)
        myDict = {'products': products}
        return render(request, 'product_detail.html', myDict)
    else:
        return HttpResponse("Hello")


@login_required(login_url="/accounts/login/")
def place_order(request, id=None):
    if id:
        prod = product.objects.filter(id=id)
        return HttpResponse("place_order method Enabled")
    else:
        return redirect('homePage')
