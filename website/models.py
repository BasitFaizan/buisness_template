from django.db import models
from django.db.models import Model
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)