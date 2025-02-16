from django.db import models

class Equipe(models.Model):
    Codigo_Equipe = models.CharField(
        max_length=50, blank=False, null=False, unique=False
    )
    Nome_encarregado = models.CharField(max_length=150, blank=False, null=False)
    Mebro_equipe1 = models.CharField(max_length=150, blank=True, null=True)
    Mebro_equipe2 = models.CharField(max_length=150, blank=True, null=True)
    Mebro_equipe3 = models.CharField(max_length=150, blank=True, null=True)
    Mebro_equipe4 = models.CharField(max_length=150, blank=True, null=True)
    Mebro_equipe5 = models.CharField(max_length=150, blank=True, null=True)
    Mebro_equipe6 = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Codigo_Equipe

