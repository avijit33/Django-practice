from django import forms
from django.contrib.auth.models import User 
from .models import Userinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserinfoForm(forms.ModelForm):
    class Meta():
        model = Userinfo
        fields = ('facebook_id', 'profile_pic')
