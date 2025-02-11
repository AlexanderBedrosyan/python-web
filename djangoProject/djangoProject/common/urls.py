from django.urls import path, include

from djangoProject.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share'),
]

