from django.db import models

# Create your models here.


class issue(models.Model):
    STATUS_CHOICS = (
        ("open", "open"),
        ("closed", "closed"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    mobile = models.IntegerField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICS, default="open")

    def __str__(self):
        return self.email
