from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, URLForm
from .models import UserProfile, URL
import random
import string

def generate_short_url():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'shortener/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'shortener/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'shortener/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    urls = URL.objects.filter(user=request.user)
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.user = request.user
            new_url.short_url = generate_short_url()
            new_url.save()
            return redirect('dashboard')
    else:
        form = URLForm()
    return render(request, 'shortener/dashboard.html', {'form': form, 'urls': urls})

@login_required
def profile(request):
    return render(request, 'shortener/profile.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
