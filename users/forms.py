from django import forms
from django.forms.models import ModelForm
from .models import Profile, Image, Comment

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date', 'Likes', 'comments']



