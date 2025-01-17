from django.contrib import admin

from tasty_recipes_app.profiles.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass