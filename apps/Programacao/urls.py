from django.urls import path, include
from Programacao import views

urlpatterns = [
    path('programacao/cadstro', views.cadastrar_programacaoequipe, name='cadastrarprogramacapequipe'),
    path('programacao/vertoda', views.ver_programacao, name='vertodaprogramacao'),
    path('programacao/calendario', views.calendario_view, name='vertodaprogramacaoemcalendario'),
    path('programacao/atualizar/<int:pk>', views.AtualizarProgramacaoEquipes.as_view(), name='atualizarprogramacão'),
    path('programacao/deletar/<int:pk>', views.DeletarProgramacaoEquipes.as_view(), name='deletarprogramacao'),
    path('calendario-dados/', views.calendario_dados, name='calendario_dados'),
]