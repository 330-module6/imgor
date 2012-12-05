'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls.defaults import *
from portal.views import *
import portal

urlpatterns = patterns('',
    # Main web portal entrance.
    (r'^$', portal_main_page),

)