from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('final_exam.common.urls')),
    path('posts/', include('final_exam.posts.urls')),
    path('author/', include('final_exam.authors.urls')),
]
