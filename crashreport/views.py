from .models import crashReport
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def crash(request):
    response =  json.loads(request.body)
    crashreport = response.get('STACK_TRACE')
    android_ver = response.get('ANDROID_VERSION')
    brand = response.get('BRAND')

    log_cat = response.get('LOGCAT')
    model = response.get('PHONE_MODEL')
    app_version_name = response.get('APP_VERSION_NAME')
    app_verson_code = response.get('APP_VERSION_CODE')
    app_package = response.get('PACKAGE_NAME')
    product = response.get('PRODUCT')

    shared_pref = response.get('SHARED_PREFERENCES')
    available_memory = response.get('AVAILABLE_MEM_SIZE')
    total_memory = response.get('TOTAL_MEM_SIZE')
    file_path = response.get('FILE_PATH')
    user_comment = response.get('USER_COMMENT')
    device_features = response.get('DEVICE_FEATURES')
    system_settings = response.get('SETTINGS_SYSTEM')
    crash_date = response.get('USER_CRASH_DATE')
    app_start_date = response.get('USER_APP_START_DATE')
    global_settings = response.get('SETTINGS_GLOBAL')
    device_display =  response.get('DISPLAY')
    initial_config = response.get('INITIAL_CONFIGURATION')
    crash_config = response.get('CRASH_CONFIGURATION')
    environment = response.get('ENVIRONMENT')
    cr = crashReport(crash_report=crashreport, android_ver=android_ver, brand=brand, log_cat=log_cat, 
        device_model=model, app_version_name=app_version_name, app_verson_code=app_verson_code, 
        product=product, app_package = app_package, shared_pref=shared_pref, available_memory=available_memory,
        total_memory=total_memory, file_path=file_path, user_comment=user_comment, device_features=device_features,
        system_settings=system_settings, crash_date=crash_date, app_start_date=app_start_date,
        global_settings=global_settings, device_display=device_display, initial_config=initial_config,
        crash_config=crash_config, environment =environment)
    try:
        cr.save()
    except Exception,e:
        print e
    return 1
