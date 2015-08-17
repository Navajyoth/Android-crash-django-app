from django.contrib import admin

from .models import crashReport
# Register your models here.

@admin.register(crashReport)
class ReportAdmin(admin.ModelAdmin):
	list_display = ('app_package', 'app_verson_code', 'device_model', 'crash_date', )
	list_filter = ['app_package', 'app_verson_code', 'device_model', 'crash_date', ]

# admin.site.register(crashReport)
