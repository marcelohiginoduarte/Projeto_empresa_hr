import django_filters
from .models import collaborator, BancoArquivos


class collaboratorFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}


class AquivoFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}

class ArquivoFilter(django_filters.FilterSet):
    class Meta:
        model = BancoArquivos
        fields = ["EI_OC"]
