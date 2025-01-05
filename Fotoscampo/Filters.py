import django_filters
from Fotoscampo.models import FotosCampo


class FotoFilter(django_filters.FilterSet):
    projeto = django_filters.CharFilter(label="Pesquisa", lookup_expr="icontains")

    class Meta:
        model = FotosCampo
        fields = ["projeto"]
