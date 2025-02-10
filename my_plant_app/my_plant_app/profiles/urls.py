from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('details/', views.DetailsProfile.as_view(), name='details-profile'),
    path('edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
]