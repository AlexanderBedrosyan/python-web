from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.profiles.validators import StartsWithValidator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        validators=[MinLengthValidator(2)]
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[StartsWithValidator()]
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        validators=[StartsWithValidator()]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )