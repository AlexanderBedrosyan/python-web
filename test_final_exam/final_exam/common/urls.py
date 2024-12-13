from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index-page'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]