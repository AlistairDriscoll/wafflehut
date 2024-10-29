import random

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Post, UserRank
from .forms import PostForm, UserRankForm, EditForm


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


def user_page(request, username):
    """
    View to show a users profile
    """
    
    user = get_object_or_404(User, username=username)
    queryset = Post.objects.filter(author=user)
    post_count = queryset.count()

    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    
    user_rank = get_object_or_404(UserRank, user=user)
    user_form = UserRankForm(instance=user_rank)

    return render(
        request,
        "blog/user_page.html",
        {
            "username": username,
            "posts": posts,
            "user_rank": user_rank,
            "post_count": post_count,
            "user_form": user_form,
        },
    )


def write_post(request):
    """
    View for taking the PostForm data and storing it in the database
    - Checks to see if the user is autheinticated, then displays the PostForm
    - Checks to see if the form is valid, and if so saves to the database with a message stating success
    - Gets the users wafflescore and adds a point to it
    - Takes the user to their webpage where their new post should appear
    """

    if request.method == "POST":
        if request.user.is_authenticated:
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                instance = post_form.save(commit=False)
                instance.author = User.objects.get(username=request.user.username)
                instance.save()
                messages.add_message(request, messages.SUCCESS, 'Post Uploaded Succesfully!!')
                
                user_rank = get_object_or_404(UserRank, user=request.user)
                user_rank.wafflescore += 1
                user_rank.save()
                print(user_rank.wafflescore)

                return redirect('user_page', username=request.user)

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

    def capitalize(title):
        return title[0].upper() + title[1:]

    post = get_object_or_404(Post, slug=slug)
    post.title = capitalize(post.title)
    form = EditForm(instance=post)

    return render(
        request,
        "blog/view_full_post.html",
        {"post": post, "edit_form": form},
    )


def delete_post(request, slug, post_id):
    """
    View to delete a post, the 'if' statement was taken from Code Institute and edited to suit this view
    - Gets the post from the database 
    - Checks to see if the post author is the same as the request user
    - If so deletes the record and knocks the users wafflescore down a point before saving
    - Adds a message depending on if the user was authorised to delete
    - Goes back to the user page
    """

    post = get_object_or_404(Post, slug=slug)
    
    if post.author == request.user:
        post.delete()
        user_rank = get_object_or_404(UserRank, user=post.author)
        user_rank.wafflescore =- 1
        user_rank.save()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own posts!')

    return HttpResponseRedirect(reverse('user_page', kwargs={'username': post.author.username}))


def edit_post(request, post_id, slug):
    """
    View to edit a Post
    """

    post = get_object_or_404(Post, slug=slug)
    edit_form = EditForm(data=request.POST, instance=post)

    if request.method == "POST":

        if edit_form.is_valid() and post.author == request.user:
            post = edit_form.save()
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
            return redirect('view_full_post', slug=post.slug)

        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    return render(
        request,
        "blog/view_full_post.html",
        {'edit_form': edit_form, 'post': post}
    )


def edit_user(request, username):
    """
    View to edit the users details
    """

    user = get_object_or_404(User, username=username)
    user_rank = get_object_or_404(UserRank, user=user)

    if request.method == "POST":
        user_form = UserRankForm(request.POST, instance=user_rank)
        if user_form.is_valid:
            user_rank = user_form.save()
            messages.add_message(request, messages.SUCCESS, 'Details Updated!')
            
            return redirect('user_page', username=username)

        else:
            print("Form errors:", user_form.errors)
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    else:
        user_form = UserRankForm(instance=user)

    posts = Post.objects.filter(author=user)
    user_rank = get_object_or_404(UserRank, user=user)
    post_count = posts.count()


    return render(
            request,
            "blog/user_page.html",
            {
                "username": username,
                "posts": posts,
                "user_rank": user_rank,
                "post_count": post_count,
                "user_form": user_form
            },
        )
