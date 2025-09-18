from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
]