# Create your views here.
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaulttags import csrf_token
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def main_page(request):
    return render_to_response('index.html')

def register(request):
        return render_to_response('userInfo/register.html', context_instance=RequestContext(request))

def add_user(request):
    
    name = request.POST['username']
    pw = request.POST['password']
    confirm = request.POST['confirm']
    email = request.POST['email']
    if pw != confirm:
        return render_to_response('userInfo/register.html', {'error_message': 'Password does not match confirmation'}, context_instance=RequestContext(request))
    try:
        User.objects.create_user(name, email, pw)
    except IntegrityError:
        return render_to_response('userInfo/register.html', {'error_message': 'Invalid username'}, context_instance = RequestContext(request))

    return render_to_response('userInfo/register.html', {'success_message': 'Account Created!'}, context_instance = RequestContext(request))

@login_required    
def changePW(request):
    user = request.user
    
    if not request.method == "POST":
        return render_to_response('userInfo/changePW.html', {'error_message' : 'Not a valid request'}, context_instance = RequestContext(request))
    
    if not user.check_password(request.POST['password']):
        return render_to_response('userInfo/changePW.html', {'error_message' : 'You must put in the correct current password to change it'}, context_instance = RequestContext(request))
    
    if request.POST['newPW'] != request.POST['newPWConf']:
        return render_to_response('userInfo/changePW.html', {'error_message' : 'Password does not match confirmation'}, context_instance = RequestContext(request))
    
    user.set_password(request.POST['newPW'])
    user.save()
    
    return render_to_response('userInfo/changePW.html', {'success_message' : 'Password Changed!'}, context_instance = RequestContext(request))

    