from django.urls import path, include

from djangoProject.common import views

urlpatterns = [
    path('', views.home, name='home')
]

