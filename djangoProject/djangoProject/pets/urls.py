from django.urls import path, include

from djangoProject.pets import views

urlpatterns = [
    path('add/', views.add_pets, name='add-pets'),
    path('<str:username>/pet/', include([
        path('<slug:pet_slug>', views.pets_details, name='pets-details'),
        path('<slug:pet_slug>/edit', views.edit_page, name='edit-details'),
        path('<slug:pet_slug>/delete', views.delete_page, name='delete-details'),
    ]))
]

