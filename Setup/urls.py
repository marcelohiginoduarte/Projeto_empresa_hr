"""
URL configuration for Setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GestaoHR import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #login
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.home, name='homapage'),
    path('create/', views.create_Collaborator, name='createcollaborador'),
    path('view/collaborator', views.to_view_collaborator, name='viewcollaborator'),
    path('editar/collaborator/<int:pk>/', views.FazerUpdate.as_view(), name='fazerupdate'),
    path('visualizar/collaborator/<int:pk>/', views.VisualizarCollaborator.as_view(), name='visualizar'),
    path('visualizacao/teste', views.to_view_collaborator1, name='testej'),
    path('visualizar/<int:pk>/', views.visualizar_com_id, name='detalhevisualizaçao'),
    path('verdetalhe/<int:pk>/', views.DetalheView.as_view(), name='detalheviews'),
    path('verdetalhe/deletar/<int:pk>/', views.DeletarColaborador.as_view(), name='deletarcolaborador'),
    path('tset1', views.uploadfotos, name='folhadeponto'),
    path('visualizarfolhasdeponto', views.visualizar_folhas_ponto, name='visualizarfolhasdeponto'),
    path('exportar_execel', views.exportar_para_execel_colaboradores, name='exportarexecelcolaboradores'),

    path('servico/register/', views.create_servico, name='criarservico'),
    path('servico/visualizartodos/', views.visualiazer_servicos, name='visualizartodosservios'),
    path('visualizarservicos/<int:pk>/', views.ServicoUpdate.as_view(), name='verservicoind'),
    path('visualizarservicosstatus/<int:pk>/', views.ServicoUpdateStatus.as_view(), name='editarstatus'),
    path('servico/remover/<int:pk>/', views.ServicoDelete.as_view(), name='remover_servico'),
    path('servico/execel', views.servico_exportar_execel, name='exportarservicoexecel'),
    path('contar/servicos', views.intem_lista, name='contarlista'),
    path('somar/servicos', views.somar_valor_status, name='somarvalores'),
    path('servico/unitarioviews/<int:pk>/', views.servico_visualizar_com_id, name='servicounitario'),


    path('demandainterna/criar', views.createdemanda, name='demandainternacriar'),
    path('demandainterna/visualizartodas/', views.demandainternavisualizartd, name='Demandainternaviews'),
    path('demandasinternasvisualizar/<int:pk>', views.DemandaUpdate.as_view(), name='demandaupdate'),
    path('demandasinternasdeletar/<int:pk>', views.RemoverDemanda.as_view(), name='demandadelete'),
    path('demandainterna/status/<int:pk>', views.DemandainternaStatus.as_view(), name='demandaatualizarstatus'),
    path('demanainterna/execel', views.demandainterna_exportar_execel, name='demanainternaexportarexcel'),
    path('demandainterna/dash', views.dashdemandainterna, name='dashdemandainterna'),


    path('arquivo/criar', views.CreateArquivos, name='criararquivos'),
    path('arquivo/visualizar', views.visualizar_arquivos, name='visualizararquivos'),
    path('arquivo/visualizar/<int:pk>', views.ArquivoUodate.as_view(), name='visualizararquivospk'),
    path('arquivo/views/<int:pk>', views.ArquivoViews.as_view(), name='verarquivos'),


    path('logar', views.logar, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('projetoativo', views.verprojetoativo, name='projetoativo'),
    path('fotoscampo', views.upload_fotos, name='fotoscampo'),
    path('salvarprojetofoto', views.Salvar_projeto_foto, name='salvarprojetofoto'),
    path('verfotos', views.verfotos, name='vertodasasfotos'),
    path('fotos/<int:projeto_id>/', views.fotos_campo_view, name='fotos_campo'),
    path('updateprojeto/<int:pk>', views.atualizativo.as_view(), name='updatedoprojeto'),
    path('projetodelete/<int:pk>', views.Deletarprojeto.as_view(), name='deletarprojetofoto'),

    path('sesmt', views.crearsesmt, name='criarsesmt'),
    path('versesmt/', views.versesmt, name='mostrararquivossesmt'),
    path('updatesesmt/<int:pk>/', views.SesmtUpdate.as_view(), name='vertodosarquivosesmts'),
    path('versaoarquivo/<int:arquivo_id>/', views.atualizararquivo, name='versaodosarquivos'),
    path('upload/', views.DocumentCreateView.as_view(), name='document-upload'),
    path('update/<int:pk>/', views.DocumentUpdateView.as_view(), name='document-update'),
    path('list/', views.DocumentListView.as_view(), name='document-list'),

    path('estoque/', views.listar_produtos, name='listarestoque'),
    path('estoquemovimentacao/<int:produto_id>', views.movimentacao_estoque, name='movimentacaoestoque'),
    path('estoquecadastra/', views.cadastra_produto, name='cadastrarproduto'),
    path('estoqueregistromovimentacao', views.registro_movimentacao, name='registro_movimentacao'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
