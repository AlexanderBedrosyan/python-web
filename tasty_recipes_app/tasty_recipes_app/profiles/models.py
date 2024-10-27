from django.core.validators import MinLengthValidator
from django.db import models

from tasty_recipes_app.profiles.validators import UpperValueValidator


# Create your models here.

class Profile(models.Model):
    nickname = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=20,
        validators=[MinLengthValidator(2, "Nickname must be at least 2 chars long!")]
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[UpperValueValidator()]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[UpperValueValidator()]
    )
    chef = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )