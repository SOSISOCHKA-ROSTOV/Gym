from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Lite(models.Model):
    workout = models.CharField(max_length=50)
    approach = models.CharField(max_length=50)


class Medium(models.Model):
    workout = models.CharField(max_length=50)
    approach = models.CharField(max_length=50)

