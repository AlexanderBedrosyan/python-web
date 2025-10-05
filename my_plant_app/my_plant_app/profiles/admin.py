from django.contrib import admin

from my_plant_app.profiles.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass