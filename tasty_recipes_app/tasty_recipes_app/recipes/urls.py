from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('<int:id>/', include([
        path('details/', views.RecipeDetails.as_view(), name='details-recipe'),
        path('edit/', views.EditRecipeView.as_view(), name='edit-recipe'),
        path('delete/', views.DeleteRecipeView.as_view(), name='delete-recipe')
    ]))
]