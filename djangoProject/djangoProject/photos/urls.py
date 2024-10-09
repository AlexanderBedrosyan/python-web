from django.urls import path, include

from djangoProject.photos import views

urlpatterns = [
    path('add', views.add, name='photos_add'),
    path('<int:pk>', include([
        path('', views.details, name='details'),
        path('edit', views.edit, name='edit'),
    ]))
]

