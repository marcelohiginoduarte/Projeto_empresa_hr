import django_filters
from .models import collaborator


class collaboratorFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}


class AquivoFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {"Nome": ["icontains"]}


