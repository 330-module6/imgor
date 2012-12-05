'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls.defaults import *
from django.contrib.auth.views import login
from userInfo.views import *

urlpatterns = patterns('',
    (r'^$', main_page),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^portal/', include('portal.urls')),

)