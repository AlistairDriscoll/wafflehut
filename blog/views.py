from django.shortcuts import render
from django.views import generic
from .models import Post
import random

# Create your views here.

class index(generic.ListView): 
    posts = Post.objects.all()
    
    def get_posts(posts):
        """
        Function to return four random posts to be displayed on the home page
        """
        post_list = []
        for p in posts:
            post_list.append(p)
        display_posts = random.sample(post_list, 4)
        
        return display_posts

    
    queryset = get_posts(posts)
    template_name = "blog/posts.html"