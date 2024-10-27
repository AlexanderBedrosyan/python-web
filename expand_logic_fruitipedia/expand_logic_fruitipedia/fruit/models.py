from django.core.validators import MinLengthValidator
from django.db import models
from expand_logic_fruitipedia.fruit.validators import IsValueValidator
from expand_logic_fruitipedia.profiles.models import Profile


# Create your models here.


class Fruit(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30,
        validators=[MinLengthValidator(2), IsValueValidator()],
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        }
    )
    image = models.URLField(
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    nutrition = models.TextField(
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='fruits'
    )