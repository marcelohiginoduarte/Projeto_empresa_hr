from typing import Any
from django import forms
from GestaoHR.models import collaborator, Aquivo, Servico, DemandaInterna, BancoArquivos, FotosCampo

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = collaborator
        fields = ['Nome', 'CPF', 'RG', 'Data_contratacao', 'Servico', 'CNH', 'Vencimento_CNH', 'Data_contratacao', 'matricula', 'ASO', 'validade_aso', 'PIS', 'Salario', 'Controle_folha_ponto', 'Seguro_de_vida']
        

class testform(forms.ModelForm):
    class Meta:
        model = Aquivo
        fields = ['Nome','Arquivo_ponto','Mes','Ano']


class Servicoform(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['Numero_Servico', 'PEP', 'Servico', 'Mês_servico', 'Ano_servico','data_da_solicitacao', 'Municipio', 'Endereco', 'Status','data_programacao', 'Valor_parcial', 'Valor_final', 'desenho_servico','foto_antes', 'foto_depois' , 'Observacao']

class DemandaInternaform(forms.ModelForm):
    class Meta:
        model = DemandaInterna
        fields = ['Atividade', 'tipo', 'responsavel', 'status', 'data_solicitacao', 'data_conclusão', 'responsavel_demanda', 'arquivos', 'Observacao','arquivos_complementar', 'arquivos_complementar1', 'arquivos_complementar2']


class BancoArquivoform(forms.ModelForm):
    class Meta:
        model = BancoArquivos
        fields = ['EI_OC', 'tipo','municipio','Responsavel', 'AS_Biult', 'Medicao', 'DWG', 'AES', 'ACOS']

class FotosCampoform(forms.Form):
    class Meta:
        model = FotosCampo
        fields = ['Poste_antes', 'Poste_depois', 'cava_antes', 'cava_depois', 'GPS_antes', 'GPS_depois', 'Estrutura_antes', 'Estrutura_depois', 'panoramica', 'Equipamento_antes', 'Equipamento_depois']
    