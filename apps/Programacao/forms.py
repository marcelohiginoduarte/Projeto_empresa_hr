from django import forms
from Programacao.models import ProgramacaoEquipes


class ProgramacaoEquipeForm(forms.ModelForm):
    class Meta:
        model = ProgramacaoEquipes
        fields = [
            "SI_OC",
            "Nota_PM",
            "Ordem_execucao",
            "Status_sistema",
            "Status_campo",
            "QTD",
            "Prio_DEF",
            "Grupo_DEF",
            "Alimentador",
            "GPS_POSTE",
            "linkmaps",
            "tipo_servico",
            "Local",
            "Endereco",
            "tipo_EQP",
            "Encarregado",
            "dia",
            "Mes",
            "ANO",
            "turno",
            "prazo",
            "valor_prev",
            "valor_final",
        ]
