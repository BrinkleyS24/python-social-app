from django.urls import path
from main_app import views
from main_app.views import PostList, PostDetail, PostEdit, PostDelete, CommentDelete, Profile, ProfileEdit
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', PostList.as_view(), name='home'),
    path('home/post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('home/post/<int:pk>/edit', PostEdit.as_view(), name='post-edit'),
    path('home/post/<int:pk>/delete', PostDelete.as_view(), name='post-delete'),
    path('home/post/<int:post_pk>/comment/delete/<int:pk>/', CommentDelete.as_view(), name='comment-delete'),

    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEdit.as_view(), name='profile-edit'),



    path('accounts/signup/', views.signup, name='signup'),
]