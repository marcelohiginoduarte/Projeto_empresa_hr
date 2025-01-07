from django.db import models


class ItemServico(models.Model):
    iten = models.CharField(max_length=3)
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    QTD = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
