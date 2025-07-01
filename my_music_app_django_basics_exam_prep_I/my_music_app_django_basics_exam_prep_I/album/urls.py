from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', views.AddView.as_view(), name="add-album" ),
    path('<int:pk>/details/', views.DetailsView.as_view(), name="details-album" ),
    # path('<pk:int>/edit/', views.EditView.as_view(), name="edit-album" ),
    # path('<pk:int>/delete/', views.DeleteAlbumView.as_view(), name="delete-album" ),
]