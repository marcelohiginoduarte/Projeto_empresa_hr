from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from Equipe.models import Equipe


class collaborator(models.Model):
    tipo_servico = [
        ("Administrativo", "Administrativo"),
        ("Operacional", "Operacional"),
    ]
    Nome = models.CharField(max_length=150, blank=False, null=False)
    CPF = models.CharField(max_length=22, unique=False, blank=False, null=False)
    RG = models.CharField(max_length=12, unique=False, blank=True, null=True)
    Servico = models.CharField(max_length=20, choices=tipo_servico)
    CNH = models.CharField(max_length=12, blank=True, null=True)
    Vencimento_CNH = models.DateField(blank=True, null=True)
    Data_contratacao = models.DateField(blank=True, null=True)
    Data_ferias = models.DateField()
    matricula = models.CharField(max_length=15, blank=True, null=True, unique=True)
    ASO = models.FileField(upload_to="media/ASO/", blank=True, null=True)
    validade_aso = models.DateField()
    PIS = models.CharField(max_length=15, blank=True, null=True)
    Salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    Controle_folha_ponto = models.FileField(
        upload_to="media/Controle_folha_ponto/", blank=True, null=True
    )
    Seguro_de_vida = models.FileField(
        upload_to="media/Seguro_vida/", blank=True, null=True
    )

    def calcular_data_ferias(self):
        data_ferias = self.Data_contratacao + timedelta(days=365)
        return data_ferias

    def save(self, *args, **kwargs):
        self.Data_ferias = self.calcular_data_ferias()
        super().save(*args, **kwargs)

    def datafutura(self):
        super().clean()
        if self.Vencimento_CNH < timezone.now().date():
            raise ValidationError("A data deve ser uma data futura")

    def __str__(self):
        return self.Nome

    class Meta:
        permissions = [
            ("acesso_rh", "Acesso ao departamento de RH"),
        ]

class arquivos_foto(models.Model):
    projeto = models.CharField(max_length=25, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.projeto


class Caderno_servico(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to="media/cadernoservico/")

    def __str__(self):
        return self.nome