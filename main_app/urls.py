from django.urls import path
from . import views
from .views import PostList, PostDetail, PostEdit, PostDelete, CommentDelete, Profile, ProfileEdit
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.PostList.as_view(), name='home'),
    path('home/post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('home/post/<int:pk>/edit', views.PostEdit.as_view(), name='post-edit'),
    path('home/post/<int:pk>/delete', views.PostDelete.as_view(), name='post-delete'),
    path('home/post/<int:post_pk>/comment/delete/<int:pk>/', views.CommentDelete.as_view(), name='comment-delete'),

    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('profile/<int:pk>/edit', views.ProfileEdit.as_view(), name='profile-edit'),

    path('profile/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),


    path('accounts/signup/', views.signup, name='signup'),
]