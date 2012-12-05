# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from images.models import Image, Tag
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

def index(request):
    tag_list = sorted(Tag.objects.all())
    return render_to_response('tagList/index.html', {'tag_list': tag_list})
    
def listPics(request, tag_id):
    t = get_object_or_404(Tag, pk=tag_id)
    image_list = t.image_set.all()
    return render_to_response('tagList/listPics.html', {'image_list': image_list, 'tag': t})