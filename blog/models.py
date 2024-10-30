from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`
    The model detail here partly taken from the 'I think therfore I blog' code institute module
    """
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"


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
