from django.shortcuts import render, reverse
from django.views import generic

from .models import Post
from django.contrib.auth.models import User
import random

from django.http import HttpRequest

# Create your views here.

class Index(generic.ListView): 
    posts = Post.objects.all()
    
    def get_posts(posts):
        """
        Function to return four random posts to be displayed on the home page
        """

        post_list = []
        for p in posts:
            post_list.append(p)
        
        if len(post_list) >= 4:
            display_posts = random.sample(post_list, 4)
        else:
            display_posts = post_list
        
        return display_posts

    
    queryset = get_posts(posts)
    template_name = "blog/posts.html"


def user_page(request):
    username = request.user
    queryset = Post.objects.filter(author=username)

    return render(
        request,
        "blog/user_page.html",
        {"username": username,"posts": queryset},
    )
    
    