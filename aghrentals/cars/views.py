from django.shortcuts import render
from products.models import product, Company

# Create your views here.


def carHome(request, company=None):
    products = None
    if company:
        products = product.objects.filter(
            category='car', company__name=company)
    else:
        products = product.objects.filter(
            category='car')
    companies = Company.objects.filter(category='car')
    myDict = {'companies': companies, 'products': products}
    return render(request, "carHome.html", myDict)
