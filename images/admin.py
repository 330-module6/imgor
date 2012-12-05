'''
Created on Dec 5, 2012

@author: Mason
'''
from images.models import Image, Tag
from django.contrib import admin

admin.site.register(Image)
admin.site.register(Tag)