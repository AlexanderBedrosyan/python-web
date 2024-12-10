from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('<int:id>/', include([
        path('details/', views.DetailsPostView.as_view(), name='post-details'),
        path('edit/', views.EditPostView.as_view(), name='post-edit'),
        path('delete/', views.DeletePostView.as_view(), name='post-delete'),
    ]))
]