from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout

from OASystem import settings
from oa.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^OASystem/', include('OASystem.foo.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^accounts/login/$',login,{'template_name': 'oa/login.html'}),
    (r'^accounts/logout/$', logout,{'template_name': 'oa/logout.html'}),
    (r'^accounts/profile/$',index),

    (r'^oa/', include('OASystem.oa.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
