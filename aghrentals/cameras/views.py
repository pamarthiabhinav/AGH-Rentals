from django.shortcuts import render
from products.models import product, Company

# Create your views here.


def cameraHome(request, company=None):
    products = None
    if company:
        products = product.objects.filter(
            category='camera', company__name=company)
    else:
        products = product.objects.filter(
            category='camera')
    companies = Company.objects.filter(category='camera')
    myDict = {'companies': companies, 'products': products}
    return render(request, "cameraHome.html", myDict)
