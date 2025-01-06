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
                            exportar_para_execel_colaboradores,
                            CreateArquivos,
                            visualizar_arquivos,
                            ArquivoUodate,
                            ArquivoViews,
                            logar,
                            logout_view,
                            )
from django.conf.urls.static import static 
from django.conf.urls import handler403
from django.conf import settings
from django.contrib.auth import views as auth_views
from GestaoHR.views import permission_denied_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homapage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('demandainterna/', include('demandainterna.urls')),
    path('servico/', include('Servico.urls')),
    path('equipe', include('Equipe.urls')),
    path('arquivo', include('Arquivo.urls')),
    path('fotoscampo', include('Fotoscampo.urls')),
    path('sesmt', include('Sesmt.urls')),
    path('estoque', include('Estoque.urls')),
    path('programacao', include('Programacao.urls')),

    path('create/', create_Collaborator, name='createcollaborador'),
    path('view/collaborator', to_view_collaborator, name='viewcollaborator'),
    path('editar/collaborator/<int:pk>/', FazerUpdate.as_view(), name='fazerupdate'),
    path('visualizar/collaborator/<int:pk>/', VisualizarCollaborator.as_view(), name='visualizar'),
    path('visualizacao/teste', to_view_collaborator1, name='testej'),
    path('visualizar/<int:pk>/', visualizar_com_id, name='detalhevisualizaçao'),
    path('verdetalhe/<int:pk>/', DetalheView.as_view(), name='detalheviews'),
    path('verdetalhe/deletar/<int:pk>/', DeletarColaborador.as_view(), name='deletarcolaborador'),
    path('exportar_execel', exportar_para_execel_colaboradores, name='exportarexecelcolaboradores'),
    path('arquivo/criar', CreateArquivos, name='criararquivos'),
    path('arquivo/visualizar', visualizar_arquivos, name='visualizararquivos'),
    path('arquivo/visualizar/<int:pk>', ArquivoUodate.as_view(), name='visualizararquivospk'),
    path('arquivo/views/<int:pk>', ArquivoViews.as_view(), name='verarquivos'),
    path('logar', logar, name='login'),
    path('logout', logout_view, name='logout'),
    
]
handler403 = permission_denied_view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

