from django import forms
from demandainterna.models import DemandaInterna


class DemandaInternaform(forms.ModelForm):
    class Meta:
        model = DemandaInterna
        fields = [
            "Atividade",
            "tipo",
            "responsavel",
            "status",
            "responsavel_demanda",
            "arquivos",
            "Observacao",
            "arquivos_complementar",
            "arquivos_complementar1",
            "arquivos_complementar2",
        ]
