from django import forms
from Estoque.models import MovimentacaoEstoque, Produto


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ["tipo", "quantidade", "realizado_para"]
        widgets = {
            "tipo": forms.Select(),
            "quantidade": forms.NumberInput(attrs={"min": 1}),
            "realizado_para": forms.TextInput(
                attrs={"placeholder": "Nome do Colaborador"}
            ),
        }
        labels = {
            "tipo": "Tipo de Movimentação",
            "quantidade": "Quantidade",
            "realizado_para": "Realizado Para",
        }


class CadastrarProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "quantidade", "categoria", "codigo"]

