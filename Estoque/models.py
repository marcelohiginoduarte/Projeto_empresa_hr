from django.db import models

class Produto(models.Model):

    TIPO_CATEGORIA = [
        ("EPI", "EPI"),
        ("EPC", "EPC"),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.CharField(
        max_length=50,
        choices=TIPO_CATEGORIA,
    )
    codigo = models.CharField(max_length=100, unique=False)
    data_entrada = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class MovimentacaoEstoque(models.Model):
    TIPOS_MOVIMENTACAO = [
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPOS_MOVIMENTACAO)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)
    realizado_para = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} - {self.quantidade}"

    class Meta:
        permissions = [
            ("acesso_gestaoestoque", "Acesso as gestão de estoque"),
        ]
