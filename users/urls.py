from django.urls import path
from .views import home, profile, upload, show_image

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('new/upload/', upload, name='upload'),
    path('image/<int:id>', show_image, name='show_image')
]