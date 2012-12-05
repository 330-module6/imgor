'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('tagList.views', 
    url(r'^(?P<tag_id>\d+)/$', 'recentImage' ,name='most_recent'),
    url(r'^(?P<tag_id>\d+)/(?P<last_image_id>.*)/$', 'recentImage', name='somewhat_recent'),
)