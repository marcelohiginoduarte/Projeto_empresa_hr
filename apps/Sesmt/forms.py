from django import forms
from Sesmt.models import SESMT, ArquivoSesmt, Document


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