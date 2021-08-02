from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http.request import host_validation_re

# Create your models here.

class User(AbstractUser):
    userpoint = models.IntegerField(max_length=100, default=0)
    korname = models.CharField(max_length=100)
    # otpdata = models.IntegerField(default=0)
    usenums = models.IntegerField(default=0)
    phonenum = models.CharField(max_length=100, default=0)
    auth = models.CharField(max_length=100)
    forevent = models.IntegerField(max_length=10, default=0)



class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class history(models.Model):
    u_id = models.CharField(max_length=100)
    s_id = models.CharField(max_length=100)
    nowpoint = models.IntegerField(max_length=100, default=0)
    h_date = models.CharField(max_length=100)