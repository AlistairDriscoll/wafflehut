In the future I wish to implement a Comment model and a Reaction model, both would be for the Post model. The Post and Comment ratio would be a many-to-one in order for the post to have several comments, and the Reaction model would have to be a many-to-many relationship given that lots of different posts can have lots of different reactions. Furthermore, in order to make sure each user can only put one post per page as would be the case if I left the models as described, I then could make another model that creates as instance of a UserReaction that imports the User, Post and Reaction as foreign keys and makes sure that the Meta class has the post and user to be unique together. The extra models are demonstrated below.


```python
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

    REACTIONS = (
        (0, "This is absolute complete waffle"),
        (1, "This is pretty much waffle"),
        (2, "I neither agree nor disagree with this waffle"), 
        (3, "I fully agree with this waffle")
    )

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
```

Then the Comment form would go on to look as so:


```python
    class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
```

The Comment form and other comments would be displayed on the full post as so:

```
{% if user.is_authenticated %}
<p>Want to reply to this waffle?</p>
<form id="commentForm" method="post">
  {% csrf_token %}
  {{ comment_form | crispy }}
  <button type="submit" id="postComment" class="btn btn-signup btn-lg">Submit Comment</button>
</form>
{% endif %}


{% for comment in comments %}

{{ comment.author }}
{{ comment.body }}
{{ comment.created_on }}

{% endfor %}

```

The posting functionality for the Comment form would be within the 'view_full_post' view/template as that is where the form would post.

```python

    if request.method == "POST":
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.author = request.user
                instance.post = post
                instance.save()
                messages.add_message(request, messages.SUCCESS, 'Comment posted successfully!!')


                user_rank = get_object_or_404(UserRank, user=request.user)
                user_rank.wafflescore += 1
                user_rank.save()

                return redirect('view_full_post', slug=slug,)
```