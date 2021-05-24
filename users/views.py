from json.encoder import JSONEncoder
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, NewImageForm, CommentModelForm
from .models import Profile, Image, Like, Comment
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .email import send_confirm_email

@login_required
def home(request):
     # get logged in user profile
    profile = Profile.objects.get(user=request.user)

    # check who we are following
    users = [user for user in profile.following.all()]

    # initial values for vars
    images = []
    qs = None

    # get the posts of people we are following
    for u in users:
        p = Profile.objects.get(user=u)
        p_images = p.images.all()
        images.append(p_images)
    
    # our posts
    my_posts = profile.profile_images()
    images.append(my_posts)
    return render(request, 'insta/home.html', {'profile': profile, 'images': images})


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
            image.profile = current_user.profile
            image.save()
        return redirect('home')
    else:
        form = NewImageForm()
    return render(request, 'insta/upload.html', {"form": form})


def show_image(request, id):
    image = Image.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            image_id = request.POST.get('image_id')
            comment.image = Image.objects.get(id=image_id)
            comment.save()
            form = CommentModelForm()
            return redirect('show_image', image.id)
    else:
        form = CommentModelForm()
    return render(request, 'insta/image_details.html', {"image": image, "profile": profile, "form": form})


@login_required
def image_like(request):

    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_obj = Image.objects.get(id=image_id)
        # profile = Profile.objects.get(user=user)

    if user in image_obj.Likes.all():
        image_obj.Likes.remove(user)
    else:
        image_obj.Likes.add(user)
        like, created = Like.objects.get_or_create(user=user, image_id=image_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
        image_obj.save()
        like.save()
    return redirect('home')


def search_results(request):
    keyword = request.GET.get('image')
    images = Image.search_by_term(keyword)
    message = f"{keyword}".capitalize()
    return render(request, 'insta/search.html', {"message": message, "images": images})

def follow_unfollow(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('newprofile')


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/peoplelist.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)

        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context['follow'] = follow
        return context

def confirmation(request):
    user = request.user
    email = user.email
    send_confirm_email(user, email)
    HttpResponseRedirect('login')

