from django.db import models


class collaborator(models.Model):
    Nome = models.CharField(max_length=150, blank=False, null=False)
    CPF = models.CharField(max_length=11, unique=True)
    Data_contratacao = models.DateField(blank=True, null=True)





    def __str__(self):
        return self.Nome
    
