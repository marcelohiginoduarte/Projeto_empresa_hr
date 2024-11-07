from typing import Any
from django import forms
from GestaoHR.models import collaborator, Aquivo, Servico, DemandaInterna, BancoArquivos, FotosCampo, arquivos_foto, SESMT, ArquivoSesmt, arquivos_foto, Document, MovimentacaoEstoque, Produto, Equipe, ProgramacaoEquipes
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
        fields = ['Tipo_investimento','Numero_Servico','Status','tipo_servico','Equipe','Status_SAP', 'Status','PEP', 'Servico', 'Mês_servico', 'Ano_servico', 'data_da_solicitacao','data_programacao', 'tecnico',  'Endereco', 'Municipio', 'Medicao','As_built','AES_ACOS','evidencias','Requisicao_ODD','Requisicao_ODI', 'Valor_parcial', 'Valor_final','Valor_pago', 'desenho_servico','foto_antes', 'foto_depois' , 'Observacao']

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
        fields = ['projeto','poste', 'Data', 'Supervisor','Equipe', 'Cidade', 'Endereco', 'ocorrencia', 'servico', 'horario_inicio', 'GPS','horario_fim' ,'Poste_antes', 'Poste_depois', 'cava_antes', 'cava_depois', 'GPS_antes', 'GPS_depois', 'Estrutura_antes', 'Estrutura_depois', 'panoramica', 'Equipamento_antes', 'Equipamento_depois', 'Numero_serie_antes', 'Numero_serie_depois', 'Numero_sap_antes', 'Numero_sap_depois','Numero_placa_antes', 'Numero_placa_depois', 'Poda_antes', 'Poda_depois', 'concreto_calcada_antes', 'concreto_calcada_depois', 'Tela_Ocorencia', 'Trajeto']
        
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
        fields = ['tipo', 'quantidade', 'realizado_para']  
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

class CadastraEquipeform(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['Codigo_Equipe', 'Nome_encarregado', 'Mebro_equipe1', 'Mebro_equipe2', 'Mebro_equipe3', 'Mebro_equipe4', 'Mebro_equipe5', 'Mebro_equipe6']


class ProgramacaoEquipeForm(forms.ModelForm):
    class Meta:
        model = ProgramacaoEquipes
        fields = ['SI_OC', 'Nota_PM', 'Ordem_execucao', 'Status_sistema', 'Status_campo', 'QTD', 'Prio_DEF', 'Grupo_DEF', 'Alimentador', 'GPS_POSTE', 'linkmaps', 'tipo_servico', 'Local', 'Endereco', 'tipo_EQP', 'Encarregado', 'dia', 'Mes', 'ANO', 'turno','prazo', 'valor_prev', 'valor_final']