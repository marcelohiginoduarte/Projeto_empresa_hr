import django_filters
from .models import collaborator, BancoArquivos, DemandaInterna, FotosCampo


class collaboratorFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}


class AquivoFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}



class DemandaFilter(django_filters.FilterSet):
    class Meta:
        model = DemandaInterna
        fields = {
            "Atividade": ["icontains"],
            "status": ["exact"],
        }


class ArquivoFilter(django_filters.FilterSet):
    class Meta:
        model = BancoArquivos
        fields = ["EI_OC"]


class FotoFilter(django_filters.FilterSet):
    projeto = django_filters.CharFilter(label="Pesquisa", lookup_expr="icontains")

    class Meta:
        model = FotosCampo
        fields = ["projeto"]
