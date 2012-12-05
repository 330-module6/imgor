from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    up_date = models.DateTimeField('date uploaded')
    hits = models.IntegerField()
    
    def __unicode__(self):
        return self.title