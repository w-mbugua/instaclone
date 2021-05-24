from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    photo = CloudinaryField('image')
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    following = models.ManyToManyField(User, blank=True, related_name='following')
    created = models.DateTimeField(auto_now_add=True)
    

    def profile_images(self):
        return self.images.all()

    def __str__(self):
        return f"{self.user.username} Profile"

    
    def get_images(self):
        return self.images.all()   

    @classmethod
    def get_profile_by_name(cls, username):
        profile = cls.objects.filter(user__username = username)
        return profile
    
    class Meta:
        ordering = ('-created',)


class Image(models.Model):
    
    image_name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    Likes = models.ManyToManyField(User, related_name='likes', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    img = CloudinaryField('image')

    def __str__(self):
        return self.image_name
    
    def count_likes(self):
        return self.Likes.all().count()
    
    def count_comments(self):
        return self.comment_set.all().count()
    
    @classmethod
    def search_by_term(cls, search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, caption):
        self.caption = caption

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    body = models.CharField(max_length=250, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.body[:20])



LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.image}-{self.value}"








    
    


