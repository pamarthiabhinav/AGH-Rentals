from django.db import models
from django.contrib.auth.models import User
from products.models import product, Company
from simple_history.models import HistoricalRecords

# Create your models here.

RENT_CHOICES = (
    ("active", "active"),
    ("closed", "closed"),
)


class order(models.Model):
    # prod = models.ForeignKey(product, on_delete=models.CASCADE, null=False),
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False),
    prod = models.ForeignKey(product,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    bookDate = models.DateField(null=False)
    bookDays = models.IntegerField(null=False)
    status = models.CharField(
        max_length=10, choices=RENT_CHOICES, default='active')
    price = models.IntegerField(null=False)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id)
