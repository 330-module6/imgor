'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('images.views',
    url(r'^(?P<image_id>\d+)/(?P<tag_id>\d+)$', 'index'),
    url(r'^(?P<image_id>\d+)/addTag/$', 'addTag'),
    url(r'^popular/(?P<rank>.*)/$', 'popularImage'),
)