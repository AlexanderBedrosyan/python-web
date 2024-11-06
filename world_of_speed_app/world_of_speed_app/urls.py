from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('world_of_speed_app.car.urls')),
    path('', include('world_of_speed_app.common.urls')),
    path('profile/', include('world_of_speed_app.profiles.urls')),
]
