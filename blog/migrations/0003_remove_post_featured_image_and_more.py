# Generated by Django 4.2.15 on 2024-10-08 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_reaction_userreaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='userrank',
            name='user_image',
        ),
    ]