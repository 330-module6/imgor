# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from images.models import Image, Tag
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

def index(request, image_id):
    i = get_object_or_404(Image, pk=image_id)
    return render_to_response('images/index.html', {'image' : i, 'settings' : {'mediapath' : 'http://127.0.0.1:8000/media/'}},
                               context_instance=RequestContext(request))

def addTag(request, image_id):
    i = get_object_or_404(Image, pk=image_id)
    t = get_object_or_404(Tag, pk=request.POST.get("tag_id"))
    
    tags = i.tags.all()
    
    if t in tags:
        raise Http404
    else:
        i.tags.add(t)
        i.save()
        return HttpResponseRedirect(reverse('images.views.index', args=(i.id,)))