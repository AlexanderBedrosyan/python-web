from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.profiles.validators import CharactersValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 chars long!"),
            CharactersValidator()
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        default='Nema'
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )