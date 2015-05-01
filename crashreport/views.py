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

    # print (request.POST)
    cr = crashReport(crash_report=crashreport, android_ver=android_ver, brand=brand, log_cat=log_cat, device_model=model, app_version_name=app_version_name, app_verson_code=app_verson_code, product=product, app_package = app_package)
    cr.save()
    return 1
