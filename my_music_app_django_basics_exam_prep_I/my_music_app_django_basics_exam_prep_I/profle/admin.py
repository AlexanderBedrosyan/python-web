from django.contrib import admin

from my_music_app_django_basics_exam_prep_I.profle.models import Profile


# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass