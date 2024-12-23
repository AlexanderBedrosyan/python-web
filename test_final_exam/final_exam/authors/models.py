from django.core.validators import MinLengthValidator
from django.db import models

from final_exam.authors.validators import AlphaValidator, ExactSixDigitsValidator


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=40,
        validators=[MinLengthValidator(4), AlphaValidator()]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        validators=[MinLengthValidator(2), AlphaValidator()]
    )
    passcode = models.CharField(
        blank=False,
        null=False,
        validators=[ExactSixDigitsValidator()],
        help_text="Your passcode must be a combination of 6 digits"
    )
    pets_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False
    )
    info = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )