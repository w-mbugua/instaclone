from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    photo = CloudinaryField('image')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Profile"

class Image(models.Model):
    
    image_name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    Likes = models.ManyToManyField(User, related_name='images_liked', blank=True)
    comments = models.ManyToManyField(User, related_name='comments', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    img = CloudinaryField('image')

    def __str__(self):
        return self.image_name
    
    


