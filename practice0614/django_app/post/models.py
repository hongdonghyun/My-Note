from django.db import models
from django.conf import settings

from module.time_mixin import TimeMixinStamp


class Post(TimeMixinStamp):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    photo = models.ImageField(upload_to='post%y%m%d')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike',
        related_name='like_posts'

    )


class Comment(TimeMixinStamp):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
