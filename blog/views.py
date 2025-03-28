import random

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Post, UserRank
from .forms import PostForm, UserRankForm, EditForm


def index(request):
    """
    Homepage view — shows 4 random posts.
    """

    posts = list(Post.objects.all())
    if len(posts) >= 4:
        posts = random.sample(posts, 4)

    return render(
        request,
        "blog/posts.html",
        {"username": request.user, "posts": posts},
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


@login_required
def delete_account(request):
    """
    Secure view to delete the logged-in user's account.
    """
    request.user.delete()
    messages.success(request, "Account successfully deleted.")
    return redirect("index")


@login_required
def write_post(request):
    """
    View to create a post.
    Adds a waffle point and redirects to the user's page if successful.
    """
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = request.user
            if instance.content.strip() == "":
                instance.content = (
                    f"{request.user.username} has refused to"
                    " elaborate their waffle."
                )
            instance.save()

            user_rank = get_object_or_404(UserRank, user=request.user)
            user_rank.wafflescore += 1
            user_rank.save()

            messages.success(request, "Post uploaded successfully!")
            return redirect("user_page", username=request.user.username)
        else:
            messages.error(request, "There was an error with your post.")

    else:
        post_form = PostForm()

    return render(
        request,
        "blog/write_post.html",
        {"post_form": post_form},
    )


def view_full_post(request, slug):
    """
    View to display a full blog post and edit form if the user is the author
    """
    post = get_object_or_404(Post, slug=slug)

    context = {
        "post": post,
    }

    if request.user.is_authenticated and request.user == post.author:
        context["edit_form"] = EditForm(instance=post)

    return render(request, "blog/view_full_post.html", context)


@login_required
def delete_post(request, slug):
    """
    View to delete a post, the 'if' statement was taken from Code Institute and
    edited to suit this view
    - Gets the post from the database
    - Checks to see if the post author is the same as the request user
    - If so deletes the record and knocks the users wafflescore down a point
    before saving
    - Adds a message depending on if the user was authorised to delete
    - Goes back to the user page
    """

    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        user_rank = get_object_or_404(UserRank, user=post.author)
        user_rank.wafflescore -= 1
        user_rank.save()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.error(request, 'You can only delete your own posts!')

    return HttpResponseRedirect(
        reverse('user_page', kwargs={'username': post.author.username}))


@login_required
def edit_post(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id, slug=slug)

    if post.author != request.user:
        messages.warning(request, "You are not allowed to edit this post.")
        return redirect("index")

    if request.method == "POST":
        edit_form = EditForm(data=request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Post Updated!')
            return redirect('view_full_post', slug=post.slug)
        else:
            messages.error(request, 'Error updating post!')
    else:
        edit_form = EditForm(instance=post)

    return render(
        request,
        "blog/view_full_post.html",
        {'edit_form': edit_form, 'post': post}
    )


@login_required
def edit_user(request, username):
    """
    View to edit the user's profile details.
    Only allows the user to edit their own info.
    """

    user = get_object_or_404(User, username=username)
    if user != request.user:
        messages.error(
            request, "You are not allowed to edit this user's information.")
        return redirect("index")

    user_rank = get_object_or_404(UserRank, user=user)

    if request.method == "POST":
        user_form = UserRankForm(request.POST, instance=user_rank)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Details updated!")
            return redirect("user_page", username=username)
        else:
            messages.error(
                request, "There was an error updating your details.")
    else:
        user_form = UserRankForm(instance=user_rank)

    posts = Post.objects.filter(author=user)
    post_count = posts.count()

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
