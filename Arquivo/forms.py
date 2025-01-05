from django import forms
from Arquivo.models import Aquivo


class testform(forms.ModelForm):
    class Meta:
        model = Aquivo
        fields = ["Nome", "Arquivo_ponto", "Mes", "Ano"]