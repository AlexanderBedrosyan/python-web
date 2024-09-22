from django.db import models

# Create your models here.

class ToDoList(models.Model):

    title = models.CharField(max_length=40, default='Random task')
    description = models.TextField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title