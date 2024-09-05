from django.contrib import admin
from .models import Post, Comment, UserRank, Reaction


# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserRank)
admin.site.register(Reaction)