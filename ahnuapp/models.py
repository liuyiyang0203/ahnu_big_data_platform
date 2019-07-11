from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RUser(AbstractUser):
    pass

class Teacher(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=1000)
    publish = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    url_link = models.CharField(max_length=10000)