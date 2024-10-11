from django.db import models
from django.contrib.auth.models import User


REACTIONS = ((0, "This is absolute complete waffle"), (1, "This is pretty much waffle"), (2, "I neither agree nor disagree with this waffle"), (3, "I fully agree with this waffle"))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`
    The model detail here partly taken from the 'I think therfore I blog' code institute module
    """
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`
    The model detail here taken from the 'I think therfore I blog' code institute module
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class UserRank(models.Model):
    """
    Stores a single user rank entry related to :model:`auth.User`
    Partly taken from the 'I think therefore I blog' code institute module
    """
    wafflescore = models.IntegerField(default=0)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_rank"
    )
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    dof = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s User Rank"


class Reaction(models.Model):
    """
    Stores a single reaction entry related to :model:`auth.User`
    Partly taken from the 'I think therfore I blog' code institute module
    """
    reactor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reactor"
    )

    posts = models.ManyToManyField(
        Post, related_name="reactions"
    )

    reaction_option = models.IntegerField(choices=REACTIONS)


class UserReaction(models.Model):
    """
    Through model to use so that each user can only react to a post once
    Needed because the posts and reactions have a many-to-many ratio
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
