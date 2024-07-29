from django.urls import path
from .import views


urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('create/', views.media_create, name='media_create'),
    path('<int:media_id>/edit/', views.media_edit, name='media_edit'),
    path('<int:media_id>/delete/', views.media_delete, name='media_delete'),
    path('register/', views.register, name='register'),
]