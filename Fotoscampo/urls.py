from django.urls import path, include
from Fotoscampo import views

urlpatterns = [
    path('fotoscampo', views.upload_fotos, name='fotoscampo'),
    path('fotos/<str:projeto_nome>/', views.verfotos_grupadas, name='fotos_campo'),
    path('verfotos', views.verfotos, name='vertodasasfotos'),
    path('salvarprojetofoto', views.Salvar_projeto_foto, name='salvarprojetofoto'),
    path('gerar_pdf/<str:projeto_nome>/', views.gerar_pdf_fotos_grupadas, name='relatorio_pdf'),

]