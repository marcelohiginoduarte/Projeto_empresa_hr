from django.urls import path, include
from Sesmt import views

urlpatterns = [
    path('sesmt', views.crearsesmt, name='criarsesmt'),
    path('versesmt/', views.versesmt, name='mostrararquivossesmt'),
    path('updatesesmt/<int:pk>/', views.SesmtUpdate.as_view(), name='vertodosarquivosesmts'),
    path('versaoarquivo/<int:arquivo_id>/', views.atualizararquivo, name='versaodosarquivos'),
    path('upload/', views.DocumentCreateView.as_view(), name='document-upload'),
    path('update/<int:pk>/', views.DocumentUpdateView.as_view(), name='document-update'),
    path('list/', views.DocumentListView.as_view(), name='document-list'),

]