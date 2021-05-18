from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    re_path(r'^(\d+)\/details$', views.details, name="details"),
    re_path(r'^(\d+)\/edit$', views.edit, name="edit")
]