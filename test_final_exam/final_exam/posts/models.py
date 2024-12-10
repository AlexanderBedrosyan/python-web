from django.core.validators import MinLengthValidator
from django.db import models

from final_exam.authors.models import Author


# Create your models here.


class Post(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=50,
        validators=[MinLengthValidator(5)],
        error_messages={
            "unique": "Oops! That title is already taken. How about something fresh and fun?"
        }
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        help_text="Share your funniest furry photo URL!"
    )
    content = models.TextField(
        blank=False,
        null=False
    )
    update_at = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='posts'
    )