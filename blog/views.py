from django.shortcuts import render, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, UserRank
from .forms import PostForm

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
    """
    View for taking the PostForm data and storing it in the database
    """
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

def view_full_post(request, slug):
    """
    View to display a full blog post
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post.title = post.title.capitalize()

    return render(
        request,
        "blog/view_full_post.html",
        {"post": post,},
    )
    
def delete_post(request, slug, post_id):
    """
    View to delete a post, the 'if' statement was taken from Code Institute and edited to suit this view
    """

    post = get_object_or_404(Post, slug=slug)
    
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('user_page'))
    
