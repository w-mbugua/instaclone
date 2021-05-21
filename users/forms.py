from django import forms
from django.forms.models import ModelForm
from .models import Profile

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo']