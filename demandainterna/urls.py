from django.urls import path
from demandainterna import views

urlpatterns = [
    path('demandainterna/criar', views.createdemanda, name='demandainternacriar'),
    path('demandainterna/visualizartodas/', views.demandainternavisualizartd, name='Demandainternaviews'),
    path('demandasinternasvisualizar/<int:pk>', views.DemandaUpdate.as_view(), name='demandaupdate'),
    path('demandasinternasdeletar/<int:pk>', views.RemoverDemanda.as_view(), name='demandadelete'),
    path('demandainterna/status/<int:pk>', views.DemandainternaStatus.as_view(), name='demandaatualizarstatus'),
    path('demanainterna/execel', views.demandainterna_exportar_execel, name='demanainternaexportarexcel'),
    path('demandainterna/dash', views.dashdemandainterna, name='dashdemandainterna'),
    path('demandainterna/consultacadernoservico', views.consultar_servico, name='consultarcadernodeservico'),
    path('demandainterna/acos', views.preencher_acos, name='Fazeracos'),
]