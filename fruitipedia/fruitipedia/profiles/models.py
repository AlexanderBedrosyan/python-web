from django.core.validators import MinLengthValidator
from django.db import models
from .validators import StartsWithValidator

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=[MinLengthValidator(2), StartsWithValidator("Your name must start with a letter!")]
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=[MinLengthValidator(1), StartsWithValidator("Your name must start with a letter!")]
    )
    email = models.EmailField(
        null=False,
        blank=False,
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
    image = models.URLField(
        blank=True,
        null=True
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18
    )

    def __str__(self):
        return self.first_name