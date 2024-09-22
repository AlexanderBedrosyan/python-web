from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = 'to_do_app.views.custom_404'

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<task_name>/', views.task_by_name)
]