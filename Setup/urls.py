from django.contrib import admin
from django.urls import path, include
from GestaoHR.views import (home, 
                            create_Collaborator, 
                            to_view_collaborator, 
                            FazerUpdate, VisualizarCollaborator, 
                            to_view_collaborator1,
                            visualizar_com_id,
                            DetalheView,
                            DeletarColaborador,
                            uploadfotos,
                            visualizar_folhas_ponto,
                            exportar_para_execel_colaboradores,
                            createdemanda,
                            demandainternavisualizartd,
                            DemandaUpdate,
                            RemoverDemanda,
                            DemandainternaStatus,
                            demandainterna_exportar_execel,
                            dashdemandainterna,
                            consultar_servico,
                            preencher_acos,
                            CreateArquivos,
                            visualizar_arquivos,
                            ArquivoUodate,
                            ArquivoViews,
                            logar,
                            logout_view,
                            verprojetoativo,
                            upload_fotos,
                            Salvar_projeto_foto,
                            verfotos,
                            verfotos_grupadas,
                            atualizativo,
                            Deletarprojeto,
                            crearsesmt,
                            versesmt,
                            SesmtUpdate,
                            atualizararquivo,
                            DocumentCreateView,
                            DocumentUpdateView,
                            DocumentListView,
                            listar_produtos,
                            movimentacao_estoque,
                            cadastra_produto,
                            registro_movimentacao,
                            cadastrar_programacaoequipe,
                            ver_programacao,
                            calendario_view,
                            AtualizarProgramacaoEquipes,
                            DeletarProgramacaoEquipes,
                            calendario_dados,
                            FotoUploadView,
                            gerar_pdf_fotos_grupadas,

                            )
from Equipe.views import (
                    cadastrar_equipe,
                    ver_equipes,
                    AtualizarEquipe,
                    DeletarEquipe,
                    )
from Servico import views
from django.conf.urls.static import static 
from django.conf.urls import handler403
from django.conf import settings
from django.contrib.auth import views as auth_views
from GestaoHR.views import permission_denied_view



urlpatterns = [
    path('admin/', admin.site.urls),
    #login
    path('accounts/', include('django.contrib.auth.urls')),

    path('', home, name='homapage'),
    path('create/', create_Collaborator, name='createcollaborador'),
    path('view/collaborator', to_view_collaborator, name='viewcollaborator'),
    path('editar/collaborator/<int:pk>/', FazerUpdate.as_view(), name='fazerupdate'),
    path('visualizar/collaborator/<int:pk>/', VisualizarCollaborator.as_view(), name='visualizar'),
    path('visualizacao/teste', to_view_collaborator1, name='testej'),
    path('visualizar/<int:pk>/', visualizar_com_id, name='detalhevisualizaçao'),
    path('verdetalhe/<int:pk>/', DetalheView.as_view(), name='detalheviews'),
    path('verdetalhe/deletar/<int:pk>/', DeletarColaborador.as_view(), name='deletarcolaborador'),
    path('tset1', uploadfotos, name='folhadeponto'),
    path('visualizarfolhasdeponto', visualizar_folhas_ponto, name='visualizarfolhasdeponto'),
    path('exportar_execel', exportar_para_execel_colaboradores, name='exportarexecelcolaboradores'),

    path('servico/register/', views.create_servico, name='criarservico'),
    path('servico/visualizartodos/', views.visualiazer_servicos, name='visualizartodosservios'),
    path('visualizarservicos/<int:pk>/', views.ServicoUpdate.as_view(), name='verservicoind'),
    path('visualizarservicosstatus/<int:pk>/', views.ServicoUpdateStatus.as_view(), name='editarstatus'),
    path('servico/remover/<int:pk>/', views.ServicoDelete.as_view(), name='remover_servico'),
    path('servico/execel', views.servico_exportar_execel, name='exportarservicoexecel'),
    path('contar/servicos', views.intem_lista, name='contarlista'),
    path('somar/servicos', views.somar_valor_status, name='somarvalores'),
    path('servico/unitarioviews/<int:pk>/', views.servico_visualizar_com_id, name='servicounitario'),


    path('demandainterna/criar', createdemanda, name='demandainternacriar'),
    path('demandainterna/visualizartodas/', demandainternavisualizartd, name='Demandainternaviews'),
    path('demandasinternasvisualizar/<int:pk>', DemandaUpdate.as_view(), name='demandaupdate'),
    path('demandasinternasdeletar/<int:pk>', RemoverDemanda.as_view(), name='demandadelete'),
    path('demandainterna/status/<int:pk>', DemandainternaStatus.as_view(), name='demandaatualizarstatus'),
    path('demanainterna/execel', demandainterna_exportar_execel, name='demanainternaexportarexcel'),
    path('demandainterna/dash', dashdemandainterna, name='dashdemandainterna'),
    path('demandainterna/consultacadernoservico', consultar_servico, name='consultarcadernodeservico'),
    path('demandainterna/acos', preencher_acos, name='Fazeracos'),

    path('arquivo/criar', CreateArquivos, name='criararquivos'),
    path('arquivo/visualizar', visualizar_arquivos, name='visualizararquivos'),
    path('arquivo/visualizar/<int:pk>', ArquivoUodate.as_view(), name='visualizararquivospk'),
    path('arquivo/views/<int:pk>', ArquivoViews.as_view(), name='verarquivos'),


    path('logar', logar, name='login'),
    path('logout', logout_view, name='logout'),

    path('projetoativo', verprojetoativo, name='projetoativo'),
    path('fotoscampo', upload_fotos, name='fotoscampo'),
    path('salvarprojetofoto', Salvar_projeto_foto, name='salvarprojetofoto'),
    path('verfotos', verfotos, name='vertodasasfotos'),
    path('fotos/<str:projeto_nome>/', verfotos_grupadas, name='fotos_campo'),
    path('updateprojeto/<int:pk>', atualizativo.as_view(), name='updatedoprojeto'),
    path('projetodelete/<int:pk>', Deletarprojeto.as_view(), name='deletarprojetofoto'),

    path('sesmt', crearsesmt, name='criarsesmt'),
    path('versesmt/', versesmt, name='mostrararquivossesmt'),
    path('updatesesmt/<int:pk>/', SesmtUpdate.as_view(), name='vertodosarquivosesmts'),
    path('versaoarquivo/<int:arquivo_id>/', atualizararquivo, name='versaodosarquivos'),
    path('upload/', DocumentCreateView.as_view(), name='document-upload'),
    path('update/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),
    path('list/', DocumentListView.as_view(), name='document-list'),

    path('estoque/', listar_produtos, name='listarestoque'),
    path('estoquemovimentacao/<int:produto_id>', movimentacao_estoque, name='movimentacaoestoque'),
    path('estoquecadastra/', cadastra_produto, name='cadastrarproduto'),
    path('estoqueregistromovimentacao', registro_movimentacao, name='registro_movimentacao'),

    path('equipe/cadstro', cadastrar_equipe, name='cadastrarequipe'),
    path('equipe/visualizar', ver_equipes, name='vertodasequipes'),
    path('equipe/atualizar/<int:pk>', AtualizarEquipe.as_view(), name='atualizarequipe'),
    path('equipe/deletar/<int:pk>', DeletarEquipe.as_view(), name='deletarequipe'),


    path('programacao/cadstro', cadastrar_programacaoequipe, name='cadastrarprogramacapequipe'),
    path('programacao/vertoda', ver_programacao, name='vertodaprogramacao'),
    path('programacao/calendario', calendario_view, name='vertodaprogramacaoemcalendario'),
    path('programacao/atualizar/<int:pk>', AtualizarProgramacaoEquipes.as_view(), name='atualizarprogramacão'),
    path('programacao/deletar/<int:pk>', DeletarProgramacaoEquipes.as_view(), name='deletarprogramacao'),
    path('calendario-dados/', calendario_dados, name='calendario_dados'),

    path('enviodefotoapi', FotoUploadView.as_view(), name='upload-fotodecanoi'),
    
    path('gerar_pdf/<str:projeto_nome>/', gerar_pdf_fotos_grupadas, name='relatorio_pdf'),
]
handler403 = permission_denied_view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

