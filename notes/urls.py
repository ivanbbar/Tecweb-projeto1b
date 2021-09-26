from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tagsList/', views.tagsList, name='tagsList'),
    path('tag/<str:myTag>/', views.tag, name='tag'),
    path('api/notes/<int:noteId>', views.api_note),
    path('api/notes/', views.api_notes),
    path('api-auth/', include('rest_framework.urls'))
]