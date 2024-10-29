from .models import Post, UserRank, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)


class UserRankForm(forms.ModelForm):
    class Meta:
        model = UserRank
        fields = ('full_name', 'bio')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)