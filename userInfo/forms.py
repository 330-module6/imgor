'''
Created on Dec 5, 2012

@author: Mason
'''
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(require=True)
    
    class Meta:
        model = User
        fiels = ("username", "email")
        
    def post(self, request, *args, **kwargs):
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            
        