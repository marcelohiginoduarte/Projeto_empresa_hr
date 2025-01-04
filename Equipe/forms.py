from django import forms
from Equipe.models import Equipe


class CadastraEquipeform(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = [
            "Codigo_Equipe",
            "Nome_encarregado",
            "Mebro_equipe1",
            "Mebro_equipe2",
            "Mebro_equipe3",
            "Mebro_equipe4",
            "Mebro_equipe5",
            "Mebro_equipe6",
        ]