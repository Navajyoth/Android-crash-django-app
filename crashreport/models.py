from django.db import models
from datetime import datetime

# Create your models here.

class crashReport(models.Model):
    crash_report = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    android_ver = models.CharField(max_length=10000)
    brand = models.CharField(max_length=10000)
    log_cat = models.TextField(null=True)
    device_model = models.CharField(max_length=10000, null=True)
    app_version_name = models.CharField(max_length=10000, null=True)
    app_verson_code = models.CharField(max_length=10000, null=True) 
    app_package = models.CharField(max_length=10000, null=True)
    product = models.CharField(max_length=10000, null=True)

    shared_pref = models.CharField(max_length=10000, null=True)
    available_memory = models.CharField(max_length=10000, null=True)
    total_memory = models.CharField(max_length=10000, null=True)
    file_path = models.CharField(max_length=200, null=True)
    user_comment = models.TextField(null=True)
    device_features = models.TextField(null=True)
    system_settings = models.TextField(null=True)
    crash_date = models.CharField(max_length=10000, null=True)
    app_start_date = models.CharField(max_length=10000, null=True)
    global_settings = models.TextField(null=True)
    device_display =  models.TextField(null=True)
    initial_config = models.TextField(null=True)
    crash_config = models.TextField(null=True)
    environment = models.TextField(null=True)

    def __str__(self):
    	return str(self.date)
