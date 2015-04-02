from django.db import models
from datetime import datetime

# Create your models here.

class crashReport(models.Model):
    crash_report = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    android_ver = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
