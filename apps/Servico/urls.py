from django.urls import path, include
from Servico import views

urlpatterns = [
    path('servico/register/', views.create_servico, name='criarservico'),
    path('servico/visualizartodos/', views.visualiazer_servicos, name='visualizartodosservios'),
    path('visualizarservicos/<int:pk>/', views.ServicoUpdate.as_view(), name='verservicoind'),
    path('visualizarservicosstatus/<int:pk>/', views.ServicoUpdateStatus.as_view(), name='editarstatus'),
    path('servico/remover/<int:pk>/', views.ServicoDelete.as_view(), name='remover_servico'),
    path('servico/execel', views.servico_exportar_execel, name='exportarservicoexecel'),
    path('contar/servicos', views.intem_lista, name='contarlista'),
    path('somar/servicos', views.somar_valor_status, name='somarvalores'),
    path('servico/unitarioviews/<int:pk>/', views.servico_visualizar_com_id, name='servicounitario'),
]