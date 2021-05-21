from django.shortcuts import render

def home(request):
    return render(request, 'insta/home.html')

def profile(request):

    return render(request, 'insta/profile.html')