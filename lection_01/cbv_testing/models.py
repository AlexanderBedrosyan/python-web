from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Hero(models.Model):
    class CharacterOptions(models.TextChoices):
        DWARF = 'Dwarf', 'Dwarf'
        BARBARIAN = 'Barbarian', 'Barbarian'
        ORK = 'Ork', 'Ork'

    name = models.CharField(max_length=30)
    character = models.CharField(
        max_length=40,
        choices=CharacterOptions.choices
    )
    level = models.IntegerField(
        validators=[MinValueValidator(0)]
    )