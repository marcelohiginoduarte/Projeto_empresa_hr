import django_filters
from .models import collaborator, Aquivo, BancoArquivos, Servico, DemandaInterna

class collaboratorFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator
        fields = {'Nome':['icontains']}

class AquivoFilter(django_filters.FilterSet):
    class Meta:
        model = collaborator    
        fields = {'Nome':['icontains']}

class ServicoFilter (django_filters.FilterSet):
    class Meta:
        model = Servico
        fields = ['Numero_Servico', 'Mês_servico','Ano_servico'] 

class DemandaFilter(django_filters.FilterSet):
    class Meta:
        model = DemandaInterna
        fields = {'Atividade':['icontains']}

    
class ArquivoFilter(django_filters.FilterSet):
    class Meta:
        model = BancoArquivos
        fields = ['EI_OC']