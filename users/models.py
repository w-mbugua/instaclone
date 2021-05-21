from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


