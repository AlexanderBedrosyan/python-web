from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_django_basics_exam_prep_I.profle.models import Profile


# Create your models here.

class Album(models.Model):

    class AlbumChoices(models.TextChoices):
        POP_MUSIC = "Pop Music", "Pop Music"
        JAZZ_MUSIC = "Jazz Music", "Jazz Music"
        RNB_MUSIC = "R&B Music", "R&B Music"
        ROCK_MUSIC = "Rock Music", "Rock Music"
        COUNTRY_MUSIC = "Country Music", "Country Music"
        DANCE_MUSIC = "Dance Music", "Dance Music"
        HIP_HOP_MUSIC = "Hip Hop Music", "Hip Hop Music"
        OTHER = "Other", "Other"

    album_name = models.CharField(
        max_length=30,
        unique=True
    )
    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=AlbumChoices.choices
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        blank=False,
        null=False
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0.0)]
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='albums'
    )

    def __str__(self):
        return self.album_name