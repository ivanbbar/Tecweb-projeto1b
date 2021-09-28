from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.deleteNote, name='noteDelete'),
    path('edit/<int:id>', views.updateNote, name='noteEdit'),
    path('tagsList/', views.tagsList, name='tagsList'),
    path('tag/<str:myTag>/', views.tag, name='tag'),
]