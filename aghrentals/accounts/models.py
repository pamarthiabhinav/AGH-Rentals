from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.contrib.sessions.models import Session
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    propic = models.ImageField(
        upload_to="uploads/images/userprofilepics/", default="uploads/images/userprofilepics/default.png")
