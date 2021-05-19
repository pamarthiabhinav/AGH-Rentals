from django.shortcuts import render
from products.models import product, Company

# Create your views here.


def bikeHome(request, company=None):
    products = None
    if company:
        products = product.objects.filter(
            category='bike', company__name=company)
    else:
        products = product.objects.filter(
            category='bike')
    companies = Company.objects.filter(category='bike')
    myDict = {'companies': companies, 'products': products}
    return render(request, "bikeHome.html", myDict)
