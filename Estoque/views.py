from django.shortcuts import render, redirect, get_object_or_404
from Estoque.models import Produto, MovimentacaoEstoque
from django.contrib.auth.decorators import login_required, permission_required
from Estoque.forms import MovimentacaoEstoque, MovimentacaoForm, CadastrarProduto
@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "estoque_listarprodutos.html", {"produtos": produtos})


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def movimentacao_estoque(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.produto = produto
            if movimentacao.tipo == "ENTRADA":
                produto.quantidade += movimentacao.quantidade
            elif (
                movimentacao.tipo == "SAIDA"
                and produto.quantidade >= movimentacao.quantidade
            ):
                produto.quantidade -= movimentacao.quantidade
            produto.save()
            movimentacao.save()
            return redirect("listarestoque")
    else:
        form = MovimentacaoForm()
    return render(
        request, "estoque_movimentacao_estoque.html", {"produto": produto, "form": form}
    )


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def cadastra_produto(request):
    erro = None
    texto = None

    if request.method == "POST":
        form = CadastrarProduto(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("listarestoque")
    else:
        form = CadastrarProduto()
        erro = request.GET.get("erro")
        texto = request.GET.get("texto")

    return render(
        request,
        "estoque_cadastrar_produto.html",
        {"form": form, "erro": erro, "texto": texto},
    )


@login_required
@permission_required("GestaoHR.acesso_gestaoestoque", raise_exception=True)
def registro_movimentacao(request):
    movimentacao = MovimentacaoEstoque.objects.all()
    return render(
        request, "estoque_registromovimentacao.html", {"movimentacao": movimentacao}
    )
