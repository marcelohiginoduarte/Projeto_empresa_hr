from django.urls import path, include
from Arquivo import views

urlpatterns = [
    path('tset1', views.uploadfotos, name='folhadeponto'),
    path('visualizarfolhasdeponto', views.visualizar_folhas_ponto, name='visualizarfolhasdeponto'),
]