from django.contrib import admin
from .models import Profile, Image, Relationship, Comment, Like

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Relationship)
admin.site.register(Comment)
admin.site.register(Like)