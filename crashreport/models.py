from django.db import models
from datetime import datetime

# Create your models here.

class crashReport(models.Model):
    crash_report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    android_ver = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    log_cat = models.TextField(null=True)
    device_model = models.CharField(max_length=100, null=True)
    app_version_name = models.CharField(max_length=100, null=True)
    app_verson_code = models.CharField(max_length=100, null=True) 
    app_package = models.CharField(max_length=100, null=True)
    product = models.CharField(max_length=100, null=True)

    def __str__(self):
    	return str(self.date)
