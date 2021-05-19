from .models import order
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from products.models import product
import random
from datetime import datetime

# Create your views here.


@login_required(login_url="/accounts/login/")
def check_order(request, id=None):
    if id and request.method == "POST":
        prod = product.objects.filter(id=id).first()
        prod1 = product.objects.filter(id=id)
        print(prod)
        bookDays = request.POST.get("bookDays")
        request.session['bookDays'] = bookDays
        price = mp2_implementation(request, prod, bookDays)
        myDict = {"prod": prod1}
        return render(request, 'check_order.html', myDict)
    else:
        return redirect('homePage')


@login_required(login_url="/accounts/login/")
def place_order(request, id=None):
    if id and request.method == "POST":
        prod = product.objects.filter(id=id).first()
        # date = datetime.now()
        date = datetime.now()
        user = request.user
        bookDays = request.session.get("bookDays")
        price = request.session.get("totPrice")
        # print(prod.price, price, tax)
        ordr = order(user=user, prod=prod, bookDate=date,
                     bookDays=bookDays, price=price)
        ordr.save()
        # print(request.session['price'])
        del request.session['tax']
        del request.session['discount']
        del request.session['prodPrice']
        del request.session['totPrice']
        del request.session['bookDays']
        del request.session['alldayPrice']
        del request.session['withTaxPrice']
        return render(request, 'order_placed.html')
        # return HttpResponse("Your Order has Been Placed Successfully")
    else:
        pass
        return redirect('homePage')


def mp2_implementation(request, prod, bookDays):
    tax = int(bookDays) - (int(bookDays) * (random.randint(3, 9) + 1))//100
    max_disc = 3
    for i in range(5):
        max_disc = max(max_disc, calc_discount(request, prod.price))
    request.session['discount'] = max_disc*100
    fp = prod.price*24  # Calc Total Amt For A Day
    sp = (prod.price*tax)/100  # Tax Adding Amount
    request.session['tax'] = sp*100
    fsp = fp + sp
    da = (prod.price*max_disc)/100  # amount For One Day With Tax Included
    # Clac The Amt For a Day Rem Disc For bookDays
    price = int(fsp-da) * int(bookDays)
    request.session['prodPrice'] = fp
    request.session['alldayPrice'] = fp * int(bookDays)
    request.session['withTaxPrice'] = request.session['alldayPrice'] + \
        request.session["tax"]
    request.session['totPrice'] = request.session['withTaxPrice'] - \
        request.session['discount']

    # price = (prod.price*24 + ((prod.price*tax)//100)) * bookDays
    return price


def calc_discount(request, sp):
    d = len(order.objects.filter(user=request.user))
    s = str(sp)
    r = random.randint(0, len(s)-1)
    disc = (int(s[r]) * d)/20
    return disc
