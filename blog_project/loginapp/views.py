from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from loginapp.forms import SignupForm, ProfileChangeForm, ProfilepicForm

# Create your views here.

def signup(request):
    form = SignupForm()
    registered = False
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    
    dict = {'form': form, 'registered': registered}

    return render(request, 'loginapp/signup.html', dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'loginapp/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request, 'loginapp/profile.html', context={})

@login_required
def profile_change(request):
    current_user = request.user
    form = ProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = ProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request, 'loginapp/profile_change.html', context={'form':form})

@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'loginapp/pass_change.html', context={'form':form, 'changed':changed})

@login_required
def add_profile_pic(request):
    form = ProfilepicForm()
    if request.method == 'POST':
        form = ProfilepicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request, 'loginapp/profilepic_add.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilepicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilepicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request, 'loginapp/profilepic_add.html', context={'form':form})