from django.urls import path, include
from Equipe import views

urlpatterns = [
    path('equipe/cadstro', views.cadastrar_equipe, name='cadastrarequipe'),
    path('equipe/visualizar', views.ver_equipes, name='vertodasequipes'),
    path('equipe/atualizar/<int:pk>', views.AtualizarEquipe.as_view(), name='atualizarequipe'),
    path('equipe/deletar/<int:pk>', views.DeletarEquipe.as_view(), name='deletarequipe'),
]