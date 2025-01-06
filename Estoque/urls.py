from django.urls import path, include
from Estoque import views

urlpatterns = [
    path('estoque/', views.listar_produtos, name='listarestoque'),
    path('estoquemovimentacao/<int:produto_id>', views.movimentacao_estoque, name='movimentacaoestoque'),
    path('estoquecadastra/', views.cadastra_produto, name='cadastrarproduto'),
    path('estoqueregistromovimentacao', views.registro_movimentacao, name='registro_movimentacao'),
]