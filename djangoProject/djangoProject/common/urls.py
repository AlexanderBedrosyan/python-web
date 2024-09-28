from django.urls import path, include

from djangoProject.accounts import views

urlpatterns = [
    path('register/', views.register, name='register')
]

