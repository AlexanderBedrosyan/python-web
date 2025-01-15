from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile')
]