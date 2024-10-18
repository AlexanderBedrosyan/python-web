from django.db import models
from django.contrib.sessions.models import Session

# Create your models here.

class SinglePerson(models.Model):
    class GenderOption(models.TextChoices):
        MALE = 'MALE', 'MALE'
        FEMALE = 'FEMALE', 'FEMALE'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=30,
        choices=GenderOption.choices
    )
    description = models.TextField()

    class Meta:
        verbose_name = "Single Person"
        verbose_name_plural = "Single Persons"

    @property
    def average_rating(self):
        total_ratings = self.ratings.aggregate(models.Avg('rating'))['rating__avg']
        return round(total_ratings, 2) if total_ratings else 0

    def __str__(self):
        return f"{self.first_name}" + ' ' + f"{self.last_name}"


class Rating(models.Model):
    client = models.ForeignKey(SinglePerson, on_delete=models.CASCADE, related_name='ratings')
    session_key = models.CharField(max_length=40, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('client', 'session_key')

    def __str__(self):
        return f'Rating: {self.rating} for {self.client}'


class Comment(models.Model):

    client = models.ForeignKey(SinglePerson, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=30)
    comment = models.TextField()

    def __str__(self):
        return self.username