from django.urls import path
from .views import home, profile, upload

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('new/upload/', upload, name='upload'),
]