from django import forms
from GestaoHR.models import (
    collaborator,
    arquivos_foto,
)

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = collaborator
        fields = [
            "Nome",
            "CPF",
            "RG",
            "Data_contratacao",
            "Servico",
            "CNH",
            "Vencimento_CNH",
            "Data_contratacao",
            "ASO",
            "validade_aso",
            "PIS",
            "Salario",
            "Controle_folha_ponto",
            "Seguro_de_vida",
        ]





