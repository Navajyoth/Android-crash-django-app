from .models import crashReport
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def crash(request):
    crashreport = request.POST.get('STACK_TRACE')
    android_ver = request.POST.get('ANDROID_VERSION')
    brand = request.POST.get('BRAND')

    log_cat = request.POST.get('LOGCAT')
    model = request.POST.get('PHONE_MODEL')
    app_version_name = request.POST.get('APP_VERSION_NAME')
    app_verson_code = request.POST.get('APP_VERSION_CODE')
    app_package = request.POST.get('PACKAGE_NAME')
    product = request.POST.get('PRODUCT')

    shared_pref = request.POST.get('SHARED_PREFERENCES')
    available_memory = request.POST.get('AVAILABLE_MEM_SIZE')
    total_memory = request.POST.get('TOTAL_MEM_SIZE')
    file_path = request.POST.get('FILE_PATH')
    user_comment = request.POST.get('USER_COMMENT')
    device_features = request.POST.get('DEVICE_FEATURES')
    system_settings = request.POST.get('SETTINGS_SYSTEM')
    crash_date = request.POST.get('USER_CRASH_DATE')
    app_start_date = request.POST.get('USER_APP_START_DATE')
    global_settings = request.POST.get('SETTINGS_GLOBAL')
    device_display =  request.POST.get('DISPLAY')
    initial_config = request.POST.get('INITIAL_CONFIGURATION')
    crash_config = request.POST.get('CRASH_CONFIGURATION')
    environment = request.POST.get('ENVIRONMENT')


    # print (request.POST)
    cr = crashReport(crash_report=crashreport, android_ver=android_ver, brand=brand, log_cat=log_cat, 
    	device_model=model, app_version_name=app_version_name, app_verson_code=app_verson_code, 
    	product=product, app_package = app_package, shared_pref=shared_pref, available_memory=available_memory,
    	total_memory=total_memory, file_path=file_path, user_comment=user_comment, device_features=device_features,
    	system_settings=system_settings, crash_date=crash_date, app_start_date=app_start_date,
    	global_settings=global_settings, device_display=device_display, initial_config=initial_config,
    	crash_config=crash_config, environment =environment)
    cr.save()
    return 1
