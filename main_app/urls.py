from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', views.index, name='index'),
    
    path('home/', PostListView.as_view(), name='post-list'),

    path('accounts/signup/', views.signup, name='signup'),
]