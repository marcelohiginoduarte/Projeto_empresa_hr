from django import forms
from .models import Servico

class Servicoform(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            "Tipo_investimento",
            "Numero_Servico",
            "Status",
            "tipo_servico",
            "Equipe",
            "Status_SAP",
            "Status",
            "PEP",
            "Servico",
            "Mês_servico",
            "Ano_servico",
            "data_da_solicitacao",
            "data_programacao",
            "tecnico",
            "Endereco",
            "Municipio",
            "Medicao",
            "As_built",
            "AES_ACOS",
            "evidencias",
            "Requisicao_ODD",
            "Requisicao_ODI",
            "Valor_parcial",
            "Valor_final",
            "Valor_pago",
            "desenho_servico",
            "foto_antes",
            "foto_depois",
            "Observacao",
        ]
