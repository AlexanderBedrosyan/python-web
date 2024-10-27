from django.core.validators import MinLengthValidator
from django.db import models
from expand_logic_fruitipedia.profiles.validators import UpperValueValidator

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[MinLengthValidator(2), UpperValueValidator()]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[MinLengthValidator(1), UpperValueValidator()]
    )
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
        max_length=40
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text="*Password length requirements: 8 to 20 characters"
    )
    image = models.CharField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )