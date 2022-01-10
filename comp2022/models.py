from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Statistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0)
