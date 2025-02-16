import django_filters
from Arquivo.models import Aquivo
from GestaoHR.models import collaborator

class AquivoFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}