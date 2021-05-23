from json.encoder import JSONEncoder
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, NewImageForm, CommentModelForm
from .models import Profile, Image, Like, Comment
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


def home(request):
    images = Image.objects.all().order_by('-id')
    current_user = request.user
    form = CommentModelForm(request.POST) 
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = current_user
        image_id = request.POST.get('image_id')
        comment.image = Image.objects.get(id = image_id)
        comment.save()
        form = CommentModelForm() 

    return render(request, 'insta/home.html', {"images": images, "c_form": form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'insta/profile.html', {"profile": profile})

def update_profile(request):
    form = ProfileUpdateForm(request.POST, request.FILES)

    return render(request, 'insta/update_profile.html', {"form": form})

def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('home')
    else:
        form = NewImageForm()
    return render(request, 'insta/upload.html', {"form": form})

def show_image(request, id):
    image = Image.objects.get(id = id)
    profile = Profile.objects.get(user=request.user)
    return render(request, 'insta/image_details.html', {"image": image, "profile":profile})


