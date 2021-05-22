from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, NewImageForm
from .models import Profile, Image

def home(request):
    images = Image.objects.all().order_by('-id')
    return render(request, 'insta/home.html', {"images": images})

def profile(request):
    return render(request, 'insta/profile.html')

def update_profile(request):
    return

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
    return render(request, 'insta/image_details.html', {"image": image})

