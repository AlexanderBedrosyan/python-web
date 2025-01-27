from django.contrib import admin
from django.urls import path, include
from tasty_recipes_app.common import views

urlpatterns = [
    path('', views.home, name='home-page'),
]