from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WordChessCrashApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'crash/', 'crashreport.views.crash'),
    url(r'^admin/', include(admin.site.urls)),
)
