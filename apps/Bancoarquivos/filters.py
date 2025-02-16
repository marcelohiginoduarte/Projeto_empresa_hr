import django_filters
from Bancoarquivos.models import BancoArquivos

class ArquivoFilter(django_filters.FilterSet):
    class Meta:
        model = BancoArquivos
        fields = ["EI_OC"]