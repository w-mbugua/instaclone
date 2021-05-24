from django.urls import path
from .views import home, profile, upload, show_image, image_like, update_profile, search_results, ProfileListView, ProfileDetailView, follow_unfollow, confirmation

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('new/upload/', upload, name='upload'),
    path('profile/update', update_profile, name="update_profile"),
    path('image/<int:id>', show_image, name='show_image'),
    path('like/', image_like, name='like'),
    path('search/', search_results, name="image_search"),
    path('tofollow/', ProfileListView.as_view(), name="newprofile"),
    path('profile/<pk>/', ProfileDetailView.as_view(), name="newprofile-detail"),
    path('switch_follow/', follow_unfollow, name="follow-unfollow-view"),
    path('confirm/', confirmation, name='mailconfirm'),
    # path('newhome/', stream, name="newhome"),
]