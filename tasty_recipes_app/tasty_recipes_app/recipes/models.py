from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tasty_recipes_app.profiles.models import Profile


# Create your models here.


class Recipe(models.Model):
    class CuisenChoices(models.TextChoices):
        FRENCH = 'French', 'French'
        CHINESE = 'Chinese', 'Chinese'
        ITALIAN = 'Italian', 'Italian'
        BALKAN = 'Balkan', 'Balkan'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(10)],
        error_messages={
            'unique': 'We already have a recipe with the same title!'
        }
    )
    cuisine_type = models.CharField(
        blank=False,
        null=False,
        max_length=7,
        choices=CuisenChoices.choices
    )
    ingredients = models.TextField(
        blank=False,
        null=False,
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField(
        blank=False,
        null=False,
    )
    cooking_time = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes."
    )
    image = models.URLField(
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='authors'
    )