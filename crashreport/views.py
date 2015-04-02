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
    print (crashreport)
    cr = crashReport(crash_report=crashreport, android_ver=android_ver, brand=brand)
    cr.save()
    return 1
