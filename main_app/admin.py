from django.contrib import admin
from .models import Post, Comment, UserProfile, Photo

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Photo)



# Register your models here.
