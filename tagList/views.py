# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from images.models import Image, Tag
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Count
from django.contrib.auth.decorators import *

@login_required
def index(request):
    tag_list = (Tag.objects.all().annotate(num_items=Count('image')).order_by('-num_items'))
    popular_images = Image.objects.all().order_by('-hits')[:5]
    pop_items = []
    for pi, pv in enumerate(popular_images):
        pop_items.append({'rank': pi + 1, 'title': pv.title})
    return render_to_response('tagList/index.html', {'tag_list': tag_list, 'popular_list': pop_items})

@login_required    
def listPics(request, tag_id):
    t = get_object_or_404(Tag, pk=tag_id)
    image_list = t.image_set.all()
    return render_to_response('tagList/listPics.html', {'image_list': image_list, 'tag': t})

@login_required
def recentImage(request, tag_id, last_image_id=None):
    t = get_object_or_404(Tag, pk=tag_id)
    image = None
    if last_image_id == None:
        image = t.image_set.all().order_by('-up_date')[:1][0]
    else:
        last_image = get_object_or_404(Image, pk=last_image_id)
        images = t.image_set.all().exclude(up_date__gte=last_image.up_date).order_by('-up_date')[:1]
        if len(images) > 0:
            image = images[0]
        else:
            image = t.image_set.all().order_by('-up_date')[:1][0]
        
    return HttpResponseRedirect(reverse('images.views.index', kwargs={'image_id': image.id, 'tag_id': tag_id}))
