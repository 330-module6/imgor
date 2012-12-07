'''
Created on Dec 5, 2012

@author: Mason
'''
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from userInfo.views import *

urlpatterns = patterns('',
    (r'^$', main_page),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^register/$', register),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/userInfo/login/'}),
    (r'^add_user/$', add_user),
    (r'^changePW/$', changePW),
    (r'^resetPW/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/userInfo/login/'}),
    (r'^resetConfirm/(?P<uidb36>\w+)/(?<token>[\w-]/$', 'django.contrib.views.password_reset_confirm'),

)