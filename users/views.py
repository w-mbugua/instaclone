from django.shortcuts import render
from .forms import ProfileUpdateForm

def home(request):
    return render(request, 'insta/home.html')

def profile(request):
    return render(request, 'insta/profile.html')

def update_profile(request):
    return