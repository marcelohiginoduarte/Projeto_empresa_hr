from django import forms
from Bancoarquivos.models import BancoArquivos


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