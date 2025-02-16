from django.db import models
from datetime import datetime
from GestaoHR.models import collaborator

class Aquivo(models.Model):
    Mes_Mes = [
        ("Jan", "Jan"),
        ("Fev", "Fev"),
        ("Mar", "Mar"),
        ("Abr", "Abr"),
        ("Mai", "Mai"),
        ("Jun", "Jun"),
        ("Jul", "Jul"),
        ("Ago", "Ago"),
        ("Set", "Set"),
        ("Out", "Out"),
        ("Nov", "Nov"),
        ("Dez", "Dez"),
    ]
    Nome = models.CharField(
        max_length=100, blank=False, null=False
    )
    Arquivo_ponto = models.FileField(upload_to="media/imagens/Controle_folha_ponto/")
    Mes = models.CharField(max_length=6, choices=Mes_Mes, blank=False, null=False)
    matriculas = models.ForeignKey(collaborator, on_delete=models.CASCADE,  blank=False, null=False)
    Ano = models.IntegerField(default=datetime.now().year)
    idade = models.CharField(max_length=10)
