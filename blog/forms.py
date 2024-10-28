from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)