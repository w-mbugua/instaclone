from django.urls import path
from .views import home, profile, upload, show_image, image_like, update_profile

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('new/upload/', upload, name='upload'),
    path('profile/update', update_profile, name="update_profile"),
    path('image/<int:id>', show_image, name='show_image'),
    path('like/', image_like, name='like')
]