"""Signals for the blog app"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import UserRank
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_rank(sender, instance, created, **kwargs):
    if created:
        UserRank.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_rank(sender, instance, **kwargs):
    instance.userrank.save()