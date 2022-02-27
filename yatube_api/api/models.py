from django.db import models
from posts.models import Post, Comment


class CommentPost(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} {self.post}"
