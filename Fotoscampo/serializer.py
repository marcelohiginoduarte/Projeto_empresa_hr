from rest_framework import serializers
from Fotoscampo.models import FotosCampo


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotosCampo
        fields = [
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
        ]
