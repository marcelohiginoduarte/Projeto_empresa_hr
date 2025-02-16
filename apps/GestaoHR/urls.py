from django.urls import path
from GestaoHR import views

urlpatterns = [
    path('create/', views.create_Collaborator, name='createcollaborador'),
    path('view/collaborator', views.to_view_collaborator, name='viewcollaborator'),
    path('editar/collaborator/<int:pk>/', views.FazerUpdate.as_view(), name='fazerupdate'),
    path('visualizar/collaborator/<int:pk>/', views.VisualizarCollaborator.as_view(), name='visualizar'),
    path('visualizacao/teste', views.to_view_collaborator1, name='testej'),
    path('visualizar/<int:pk>/', views.visualizar_com_id, name='detalhevisualizaçao'),
    path('verdetalhe/<int:pk>/', views.DetalheView.as_view(), name='detalheviews'),
    path('verdetalhe/deletar/<int:pk>/', views.DeletarColaborador.as_view(), name='deletarcolaborador'),
    path('exportar_execel', views.exportar_para_execel_colaboradores, name='exportarexecelcolaboradores'),
    path('logar', views.logar, name='login'),
    path('logout', views.logout_view, name='logout'),
]
