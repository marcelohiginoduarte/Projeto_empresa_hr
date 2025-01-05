from django import forms
from GestaoHR.models import (
    collaborator,
    BancoArquivos,
    SESMT,
    ArquivoSesmt,
    arquivos_foto,
    Document,
    MovimentacaoEstoque,
    Produto,
    ProgramacaoEquipes,
)

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = collaborator
        fields = [
            "Nome",
            "CPF",
            "RG",
            "Data_contratacao",
            "Servico",
            "CNH",
            "Vencimento_CNH",
            "Data_contratacao",
            "matricula",
            "ASO",
            "validade_aso",
            "PIS",
            "Salario",
            "Controle_folha_ponto",
            "Seguro_de_vida",
        ]


class BancoArquivoform(forms.ModelForm):
    class Meta:
        model = BancoArquivos
        fields = [
            "EI_OC",
            "tipo",
            "municipio",
            "Responsavel",
            "AS_Biult",
            "Medicao",
            "DWG",
            "AES",
            "ACOS",
        ]





class SESMTFORM(forms.ModelForm):
    class Meta:
        model = SESMT
        fields = [
            "Brigada_emergerncia",
            "CIPA",
            "CNPJ_CRB",
            "CRB",
            "Documentacao_veiculo",
            "manual_veiculo",
            "orcamentos",
            "PCSMO",
            "prg",
            "plano_de_atendimento_emergencia",
            "plano_de_manutencao_frota",
            "POP_lM_construcao",
            "POP_LV_contrucao",
            "POP_sesmt",
            "PPCI",
            "SESMT_t",
            "Ultima_atualização",
        ]


class ArquivoSesmtForm(forms.ModelForm):
    class Meta:
        model = ArquivoSesmt
        fields = ["Nome", "arquivo"]




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["file", "version", "description"]


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ["tipo", "quantidade", "realizado_para"]
        widgets = {
            "tipo": forms.Select(),
            "quantidade": forms.NumberInput(attrs={"min": 1}),
            "realizado_para": forms.TextInput(
                attrs={"placeholder": "Nome do Colaborador"}
            ),
        }
        labels = {
            "tipo": "Tipo de Movimentação",
            "quantidade": "Quantidade",
            "realizado_para": "Realizado Para",
        }


class CadastrarProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "quantidade", "categoria", "codigo"]


class ProgramacaoEquipeForm(forms.ModelForm):
    class Meta:
        model = ProgramacaoEquipes
        fields = [
            "SI_OC",
            "Nota_PM",
            "Ordem_execucao",
            "Status_sistema",
            "Status_campo",
            "QTD",
            "Prio_DEF",
            "Grupo_DEF",
            "Alimentador",
            "GPS_POSTE",
            "linkmaps",
            "tipo_servico",
            "Local",
            "Endereco",
            "tipo_EQP",
            "Encarregado",
            "dia",
            "Mes",
            "ANO",
            "turno",
            "prazo",
            "valor_prev",
            "valor_final",
        ]
