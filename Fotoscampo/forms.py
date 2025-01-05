from django import forms
from Fotoscampo.models import FotosCampo, arquivos_foto
from django.forms import modelformset_factory

class FotosCampoform(forms.ModelForm):
    class Meta:
        model = FotosCampo
        fields = [
            "projeto",
            "poste",
            "Data",
            "Supervisor",
            "Equipe",
            "Cidade",
            "Endereco",
            "ocorrencia",
            "servico",
            "horario_inicio",
            "GPS",
            "horario_fim",
            "Poste_antes",
            "Poste_depois",
            "cava_antes",
            "cava_depois",
            "GPS_antes",
            "GPS_depois",
            "Estrutura_antes",
            "Estrutura_depois",
            "panoramica",
            "Equipamento_antes",
            "Equipamento_depois",
            "Numero_serie_antes",
            "Numero_serie_depois",
            "Numero_sap_antes",
            "Numero_sap_depois",
            "Numero_placa_antes",
            "Numero_placa_depois",
            "Poda_antes",
            "Poda_depois",
            "concreto_calcada_antes",
            "concreto_calcada_depois",
            "Tela_Ocorencia",
            "Trajeto",
        ]


FotocampoFormSet = modelformset_factory(
    FotosCampo,
    fields=(
        "projeto",
        "poste",
        "Poste_antes",
        "Poste_depois",
        "cava_antes",
        "cava_depois",
        "GPS_antes",
        "GPS_depois",
        "Estrutura_antes",
        "Estrutura_depois",
        "panoramica",
        "Equipamento_antes",
        "Equipamento_depois",
    ),
    extra=1,
)


class Projeto_fotoforms(forms.ModelForm):
    class Meta:
        model = arquivos_foto
        fields = ["projeto"]


class arquivos_fotos_projetoform(forms.ModelForm):
    class Meta:
        model = arquivos_foto
        fields = ["projeto", "ativo"]