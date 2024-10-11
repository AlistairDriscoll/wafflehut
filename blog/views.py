from django.shortcuts import render, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from .models import Post, UserRank
from .forms import PostForm
from django.contrib.auth.models import User
import random
# Create your views here.

def Index(request):
    posts = Post.objects.all()
    
    def get_posts(posts):
        """
        Function to return four random posts to be displayed on the home page
        """

        post_list = []
        for p in posts:
            if len(p.content) >= 30:
                p.content = p.content[:30] + '...'
            post_list.append(p)
        
        if len(post_list) >= 4:
            display_posts = random.sample(post_list, 4)
        else:
            display_posts = post_list
        
        return display_posts

    username = request.user
    queryset = get_posts(posts)
    
    return render(
        request,
        "blog/posts.html",
        {"username": username, "posts": queryset},
    )


def user_page(request):
    username = request.user
    queryset = Post.objects.filter(author=username)
    posts = Paginator(queryset, 4)
    user_rank = get_object_or_404(UserRank, user=request.user)
    

    return render(
        request,
        "blog/user_page.html",
        {"username": username,"posts": posts, "user_rank": user_rank},
    )

def write_post(request):
    
    
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = User.objects.get(username=request.user.username)
            instance.save()
    
    post_form = PostForm()
    
    return render(
        request,
        "blog/write_post.html",
        {"post_form": post_form},
    ) 
