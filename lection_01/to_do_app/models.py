from django.db import models

# Create your models here.

class ToDoList(models.Model):

    description = models.CharField(max_length=100)
    date = models.DateTimeField()