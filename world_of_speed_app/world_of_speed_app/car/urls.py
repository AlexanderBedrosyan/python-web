from django.urls import path, include
from . import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.CreateCarView.as_view(), name='create-car'),
    path('<int:id>/', include(
        [
            path('details/', views.CarDetailView.as_view(), name='car-details'),
            path('edit/', views.CarUpdateView.as_view(), name='edit-car'),
            path('delete/', views.CarDeleteView.as_view(), name='delete_car'),
        ]
    )),
]