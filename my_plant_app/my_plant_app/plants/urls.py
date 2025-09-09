from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreatePlantView.as_view(), name='create-plant'),
    path('details/<int:id>/', views.DetailsPlantView.as_view(), name='details-plant'),
    path('edit/<int:id>/', views.EditPlantView.as_view(), name='edit-plant'),
    path('delete/<int:id>/', views.DeletePlantView.as_view(), name='delete-plant'),
]