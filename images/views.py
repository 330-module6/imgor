# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from images.models import Image

def index(request, image_id):
    i = get_object_or_404(Image, pk=image_id)
    return render_to_response('images/index.html', {'image' : i, 'settings' : {'mediapath' : 'http://127.0.0.1:8000/media/'}})