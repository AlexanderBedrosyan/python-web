from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

from djangoProject.pets.models import Pet
from .validators import validate_file_size

# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='media',
        validators=(validate_file_size,)
    )
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(to=Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)