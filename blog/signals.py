"""Signals for the blog app, when a user is created the signals create for them their UserRank model"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import UserRank
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_rank(sender, instance, created, **kwargs):
    if created:
        UserRank.objects.create(author=instance)

@receiver(post_save, sender=User)
def save_rank(sender, instance, **kwargs):
    instance.user_rank.save()
