from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Choices Start
rentalCategory = (
    ("bike", "Bike"),
    ("camera", "Camera"),
    ("car", "Car"),
)

productStatus = (
    ("Available", "A"),
    ("Rented", "R"),
    ("Not Available", "NA"),
)

RENT_CHOICES = (
    ("active", "active"),
    ("closed", "closed"),
)
# Choices End


class Company(models.Model):
    category = models.CharField(
        max_length=10, choices=rentalCategory, null=False)
    name = models.CharField(max_length=30, null=False)
    image = models.ImageField(
        upload_to="uploads/images/companies/")

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=30, null=False)
    # company = models.CharField(max_length=30, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=10, choices=rentalCategory, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(
        max_length=20, choices=productStatus, default="available",
        help_text="A - 'Availabe'(Default)<br/>R - 'Rented'<br>NA - 'Not Availabe' ")
    price = models.IntegerField(
        null=False, help_text="Please Just Specify The Price In Rupees Per Hour Only")
    image = models.ImageField(upload_to="uploads/images/product/")

    @property
    def get_price(self):
        return self.price

    def __str__(self):
        return self.name
