from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()

class Empresa(models.Model):
    Nome_Empresa = models.CharField(max_length=100)
    Endereco = models.CharField(max_length=100)
    CNPF = models.CharField(max_length=28)