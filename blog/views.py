from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from .models import Post, UserRank
from django.contrib.auth.models import User
import random
# Create your views here.

class Index(generic.ListView): 
    posts = Post.objects.all()
    
    def get_posts(posts):
        """
        Function to return four random posts to be displayed on the home page
        """

        post_list = []
        for p in posts:
            if len(p.content) >= 50:
                p.content = p.content[:30] + '...'
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
    user_rank = get_object_or_404(UserRank, user=request.user)


    return render(
        request,
        "blog/user_page.html",
        {"username": username,"posts": queryset},
    )
    
    