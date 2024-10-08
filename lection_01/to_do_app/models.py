from django.db import models

# Create your models here.

class ToDoList(models.Model):

    title = models.CharField(max_length=40, default='Random task')
    description = models.TextField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Book(models.Model):

    title = models.CharField(
        max_length=20
    )
    author = models.CharField(
        max_length=50
    )

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
