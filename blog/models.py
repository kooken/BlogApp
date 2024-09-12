from django.conf import settings
from django.db import models

from blog.validators import validate_title, validate_age

NULLABLE = {'blank': True,
            'null': True}


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Post title",
        help_text="Type your post title here",
        validators=[validate_title]
    )

    text = models.TextField(
        max_length=1000,
        verbose_name="Blog text",
        help_text="Type your blog post here",
        **NULLABLE,
    )

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Photo",
        help_text="Attach a photo to your post",
        **NULLABLE,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Ad author",
        help_text="Choose posts' author"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of update'
    )

    def save(self, *args, **kwargs):
        validate_age(self.author)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ("-created_at", )


class Comment(models.Model):
    text = models.TextField(
        max_length=1000,
        verbose_name="Comment",
        help_text="Leave your comment here",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of creation",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of update'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Comment author",
        help_text="Choose author",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Post",
        help_text="Post to which you leave comment",
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-created_at", )
