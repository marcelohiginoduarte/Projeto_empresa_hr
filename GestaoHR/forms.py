from django import forms
from GestaoHR.models import (
    collaborator,
    BancoArquivos,
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
            "matricula",
            "ASO",
            "validade_aso",
            "PIS",
            "Salario",
            "Controle_folha_ponto",
            "Seguro_de_vida",
        ]


class BancoArquivoform(forms.ModelForm):
    class Meta:
        model = BancoArquivos
        fields = [
            "EI_OC",
            "tipo",
            "municipio",
            "Responsavel",
            "AS_Biult",
            "Medicao",
            "DWG",
            "AES",
            "ACOS",
        ]


