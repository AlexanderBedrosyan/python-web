from django.contrib import admin

from final_exam.authors.models import Author


# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass