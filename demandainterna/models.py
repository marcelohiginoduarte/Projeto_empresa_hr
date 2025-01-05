from django.db import models


class DemandaInterna(models.Model):
    tipo_atividade = [
        ("Desenho", "Desenho"),
        ("Medição", "Medição"),
        ("Verificar campo", "Verificar Campo"),
        ("Documentação", "Documentação"),
    ]

    tipo_status = [
        ("Aguardando", "Aguardando"),
        ("Andamento", "Andamento"),
        ("Realizado", "Realizado"),
        ("Correção", "Correção"),
        ("OPEX", "OPEX"),
        ("Aguardando Equatorial", "Aguardando Equatorial"),
        ("Enviado Equatorial", "Enviado Equatorial"),
        ("Aprovado Equatorial", "Aprovado Equatorial"),
        ("Correção Equatorial", "Correção Equatorial"),
    ]

    Atividade = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(
        max_length=50, choices=tipo_atividade, blank=False, null=False
    )
    responsavel = models.CharField(max_length=50, blank=True, null=True, default="")
    status = models.CharField(
        max_length=30, choices=tipo_status, blank=False, null=False
    )
    responsavel_demanda = models.CharField(
        max_length=50, blank=True, null=True, default=""
    )
    Observacao = models.TextField(max_length=200, blank=True, null=True)
    arquivos = models.FileField(
        upload_to="media/desenhoservico/Interna/", blank=True, null=True
    )
    arquivos_complementar = models.FileField(
        upload_to="media/desenhoservico/Interna/", blank=True, null=True
    )
    arquivos_complementar1 = models.FileField(
        upload_to="media/desenhoservico/Interna/", blank=True, null=True
    )
    arquivos_complementar2 = models.FileField(
        upload_to="media/desenhoservico/Interna/", blank=True, null=True
    )

    class Meta:
        permissions = [
            ("acesso_demandaInterna2", "Acesso ao gestao de demandainterna2"),
        ]
