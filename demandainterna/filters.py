import django_filters
from demandainterna.models import DemandaInterna

class DemandaFilter(django_filters.FilterSet):
    class Meta:
        model = DemandaInterna
        fields = {
            "Atividade": ["icontains"],
            "status": ["exact"],
        }