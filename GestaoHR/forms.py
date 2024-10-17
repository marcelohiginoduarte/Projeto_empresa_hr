from typing import Any
from django import forms
from GestaoHR.models import collaborator, Aquivo, Servico, DemandaInterna, BancoArquivos, FotosCampo, arquivos_foto, SESMT, ArquivoSesmt, arquivos_foto, Document, MovimentacaoEstoque, Produto
from django.forms import modelformset_factory

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

class Projeto_fotoforms(forms.ModelForm):
    class Meta:
        model = arquivos_foto
        fields = ['projeto']

class FotosCampoform(forms.ModelForm):
    class Meta:
        model = FotosCampo
        fields = ['projeto','poste' ,'Poste_antes', 'Poste_depois', 'cava_antes', 'cava_depois', 'GPS_antes', 'GPS_depois', 'Estrutura_antes', 'Estrutura_depois', 'panoramica', 'Equipamento_antes', 'Equipamento_depois', 'Numero_serie_antes', 'Numero_serie_depois', 'Numero_placa_antes', 'Numero_placa_depois', 'Poda_antes', 'Poda_depois', 'concreto_calcada_antes', 'concreto_calcada_depois']
    
FotocampoFormSet = modelformset_factory(FotosCampo, fields=('projeto','poste' ,'Poste_antes', 'Poste_depois', 'cava_antes', 'cava_depois', 'GPS_antes', 'GPS_depois', 'Estrutura_antes', 'Estrutura_depois', 'panoramica', 'Equipamento_antes', 'Equipamento_depois'), extra=1)

class SESMTFORM(forms.ModelForm):
    class Meta:
        model = SESMT
        fields = ['Brigada_emergerncia', 'CIPA', 'CNPJ_CRB', 'CRB', 'Documentacao_veiculo', 'manual_veiculo', 'orcamentos', 'PCSMO', 'prg', 'plano_de_atendimento_emergencia', 'plano_de_manutencao_frota', 'POP_lM_construcao', 'POP_LV_contrucao', 'POP_sesmt', 'PPCI', 'SESMT_t', 'Ultima_atualização']


class ArquivoSesmtForm(forms.ModelForm):
    class Meta:
        model = ArquivoSesmt
        fields = ['Nome', 'arquivo', 'versao_anterior']

class arquivos_fotos_projetoform(forms.ModelForm):
    class Meta:
        model = arquivos_foto
        fields = ['projeto', 'ativo']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'version', 'description']


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['tipo', 'quantidade', 'realizado_para']  # Adicionando o campo 'realizado_para'
        widgets = {
            'tipo': forms.Select(),
            'quantidade': forms.NumberInput(attrs={'min': 1}),
            'realizado_para': forms.TextInput(attrs={'placeholder': 'Nome do Colaborador'}),
        }
        labels = {
            'tipo': 'Tipo de Movimentação',
            'quantidade': 'Quantidade',
            'realizado_para': 'Realizado Para',
        }

class CadastrarProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'categoria', 'codigo']