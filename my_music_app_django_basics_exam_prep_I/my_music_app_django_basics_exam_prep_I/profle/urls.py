from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('details/', views.ProfileDetails.as_view(), name='profile-details'),
    path('delete/', views.ProfileDelete.as_view(), name='profile-delete'),
]