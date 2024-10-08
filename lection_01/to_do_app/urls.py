from django.urls import path
from django.conf.urls import handler404
from to_do_app import views

handler404 = 'to_do_app.views.custom_404'

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<task_name>/', views.task_by_name),
    path('forms', views.forms, name='forms'),
    path('diff_form_fields', views.diff_form_fields, name="diff_form"),
    path('inheritance_html', views.inheritance_html, name="inherit_html"),
    path('test_inherit', views.test_inherit, name="test_inherit"),
    path('custom_tag', views.custom_tag_example, name="custom_tag"),
    path('forms_advanced', views.forms_advanced, name="forms_advanced"),
    path('modelform_factory', views.modelform_factory_views, name="modelform_factory"),
]