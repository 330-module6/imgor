'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('tagList.views', 
    url(r'^(?P<tag_id>\d+)/$', 'listPics'),
)