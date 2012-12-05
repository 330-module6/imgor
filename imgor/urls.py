from django.conf.urls import patterns, include, url
from imgor import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^image/', include('images.urls')),
    url(r'^$', include('tagList.urls')),
    url(r'^tag/', include('tagList.tagUrls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':False}),
)