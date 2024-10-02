from django.apps import AppConfig
from django.db.models.signals import post_save


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        from blog.signals import create_rank, save_rank
        from django.contrib.auth.models import User
        post_save.connect(create_rank, sender=User)
        post_save.connect(save_rank, sender=User)
