from django.db import models

# Create your models here.

# Choices Start
rentalCategory = (
    ("Bike", "Bike"),
    ("Camera", "Camera"),
    ("Car", "Car"),
)
# Choices End
# Error Messages Start
Required_Error_Message = "This Field Is Required"
# Error Messages End


class product(models.Model):
    name = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=30, null=False)
    company = models.CharField(max_length=30, null=False)
    category = models.CharField(
        max_length=10, choices=rentalCategory, null=False)
    price = models.IntegerField(
        null=False, help_text="Please Just Specify The Price In Rupees Per Hour Only")

    def __str__(self):
        return self.name
