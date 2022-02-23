from django.urls import path
from . import views
from .views import PostList, PostDetail, PostEdit, PostDelete, CommentDelete

urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.PostList.as_view(), name='home'),
    path('home/post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('home/post/<int:pk>/edit', views.PostEdit.as_view(), name='post-edit'),
    path('home/post/<int:pk>/delete', views.PostDelete.as_view(), name='post-delete'),

    path('home/post/<int:post_pk>/comment/delete/<int:pk>/', views.CommentDelete.as_view(), name='comment-delete'),

    path('accounts/signup/', views.signup, name='signup'),
]