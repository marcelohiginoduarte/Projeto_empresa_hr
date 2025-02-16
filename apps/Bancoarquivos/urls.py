from django.urls import path, include
from Bancoarquivos import views

urlpatterns = [
    path('arquivo/criar', views.CreateArquivos, name='criararquivos'),
    path('arquivo/visualizar', views.visualizar_arquivos, name='visualizararquivos'),
    path('arquivo/visualizar/<int:pk>', views.ArquivoUodate.as_view(), name='visualizararquivospk'),
    path('arquivo/views/<int:pk>', views.ArquivoViews.as_view(), name='verarquivos'),
]