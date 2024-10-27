from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.car.validators import YearValidator
from world_of_speed_app.profiles.models import Profile


# Create your models here.

class Car(models.Model):
    class CarChoices(models.TextChoices):
        RALLY = "Rally", "Rally"
        OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
        KART = "Kart", "Kart"
        DRAG = "Drag", "Drag"
        OTHER = "Other", "Other"

    type = models.CharField(
        choices=CarChoices.choices,
        max_length=10,
        blank=False,
        null=False
    )
    model = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[MinLengthValidator(1)]
    )
    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[YearValidator()]
    )
    image = models.URLField(
        blank=False,
        null=False,
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1.0)]
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='owners'
    )