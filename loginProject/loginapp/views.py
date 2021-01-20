from django.shortcuts import render
from .forms import UserForm, UserinfoForm
from .models import Userinfo

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse

# Create your views here.

def index(request):
    diction = {}
    return render(request, 'loginapp/index.html', context = diction)

def login_page(request):
    return render(request, 'loginapp/login.html', context = {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('loginapp:index'))
            
            else:
                return HttpResponse("Account is not active!!")
        
        else:
            return HttpResponse("Login details are wrong!!")
    
    else:
        return HttpResponseRedirect(reverse('loginapp:login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginapp:index'))

def register(request):
    registered = False 

    if request.method == 'POST':
        user_form = UserForm(data= request.POST)
        user_info_form = UserinfoForm(data= request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            
            user_info.save()
            registered = True 
    
    else:
        user_form = UserForm()
        user_info_form = UserinfoForm()
    
    diction = {'userform':user_form, 'userinfo_form':user_info_form, 'registered':registered}
    return render(request, 'loginapp/register.html', context= diction)