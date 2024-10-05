from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass