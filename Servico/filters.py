import django_filters
from .models import Servico

class ServicoFilter(django_filters.FilterSet):
    Numero_Servico = django_filters.CharFilter(
        label="Pesquisa", lookup_expr="icontains"
    )

    class Meta:
        model = Servico
        fields = ["Numero_Servico", "Mês_servico", "Ano_servico"]

