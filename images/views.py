# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from images.models import Image, Tag
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request, image_id, tag_id):
    i = get_object_or_404(Image, pk=image_id)
    i.hits = i.hits + 1
    i.save()
    tag = get_object_or_404(Tag, pk=tag_id)
    return render_to_response('images/index.html', {'image' : i, 'settings' : {'mediapath' : 'http://127.0.0.1:8000/media/'}, 'tag': tag},
                               context_instance=RequestContext(request))

@login_required
def popularImage(request, rank):
    rank = int(float(rank))
    i = Image.objects.all().order_by('-hits')[rank-1:rank][0]
    i.hits = i.hits + 1
    i.save()
    next_rank = rank + 1
    if next_rank > 5:
        next_rank = 1
    return render_to_response('images/popular.html', {'image' : i, 'settings' : {'mediapath' : 'http://127.0.0.1:8000/media/'}, 'rank': {'my_rank': rank, 'next_rank': next_rank}},
                               context_instance=RequestContext(request))

@login_required
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