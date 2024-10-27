from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.plants.validators import IsAlphaValidator


# Create your models here.

class Plant(models.Model):
    class PlantTypeChoices(models.TextChoices):
        OUTDOOR_PLANTS = 'Outdoor Plants', 'Outdoor Plants'
        INDOOR_PLANTS = 'Indoor Plants', 'Indoor Plants'
    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[MinLengthValidator(2)],
        choices=PlantTypeChoices.choices
    )
    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[MinLengthValidator(2), IsAlphaValidator()]
    )
    image = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    price = models.FloatField(
        blank=False,
        null=False
    )