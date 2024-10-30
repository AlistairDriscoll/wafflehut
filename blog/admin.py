from django.contrib import admin
from .models import Post, UserRank
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.

admin.site.register(UserRank)

