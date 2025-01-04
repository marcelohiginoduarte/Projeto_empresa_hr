from django.db import models
from Equipe.models import Equipe
from django.db.models import Sum

class Servico(models.Model):
    tipo_servico = [
        ("Plano de Manutenção", "Plano de Manutenção"),
        ("Desenho tecnico", "Desenho tecnico"),
        ("Ocorrência", "Ocorrência"),
    ]
    tipo_status = [
        ("Programação", "Programação"),
        ("Andamento", "Andamento"),
        ("Espera", "Espera"),
        ("Concluido", "Concluido"),
        ("Fechamento", "Fechamento"),
        ("Almoxerifado", "Almoxerifado"),
        ("Pagamento", "Pagamento"),
        ("Recebido", "Recebido"),
    ]

    Mes_Mes = [
        ("Jan", "Jan"),
        ("Fev", "Fev"),
        ("Mar", "Mar"),
        ("Abr", "Abr"),
        ("Mai", "Mai"),
        ("Jun", "Jun"),
        ("Jul", "Jul"),
        ("Ago", "Ago"),
        ("Set", "Set"),
        ("Out", "Out"),
        ("Nov", "Nov"),
        ("Dez", "Dez"),
    ]

    Municipios = [
        ("ALVORADA", "ALVORADA"),
        ("ARROIO DOS RATOS", "ARROIO DOS RATOS"),
        ("BARRA DO RIBEIRO", "BARRA DO RIBEIRO"),
        ("BUTIÁ", "BUTIÁ"),
        ("CHARQUEADAS", "CHARQUEADAS"),
        ("ELDORADO DO SUL", "ELDORADO DO SUL"),
        ("GUAÍBA", "GUAÍBA"),
        ("MARIANA PIMENTEL", "MARIANA PIMENTEL"),
        ("MINAS DO LEÃO", "MINAS DO LEÃO"),
        ("PANTANO GRANDE", "PANTANO GRANDE"),
        ("PORTO ALEGRE", "PORTO ALEGRE"),
        ("SÃO JERÔNIMO", "SÃO JERÔNIMO"),
        ("VIAMÃO", "VIAMÃO"),
        ("AMARAL FERRADOR", "AMARAL FERRADOR"),
        ("ARAMBARÉ", "ARAMBARÉ"),
        ("ARROIO DO PADRE", "ARROIO DO PADRE"),
        ("ARROIO GRANDE", "ARROIO GRANDE"),
        ("BAGÉ", "BAGÉ"),
        ("BARAO DO TRIUNFO", "BARAO DO TRIUNFO"),
        ("CAMAQUÃ", "CAMAQUÃ"),
        ("CANDIOTA", "CANDIOTA"),
        ("CANGUÇU", "CANGUÇU"),
        ("CAPÃO DO LEÃO", "CAPÃO DO LEÃO"),
        ("CERRITO", "CERRITO"),
        ("CERRO GRANDE DO SUL", "CERRO GRANDE DO SUL"),
        ("CHUÍ", "CHUÍ"),
        ("CHUVISCA", "CHUVISCA"),
        ("CRISTAL", "CRISTAL"),
        ("DOM FELICIANO", "BDOM FELICIANO"),
        ("DOM PEDRITO", "DOM PEDRITO"),
        ("ENCRUZILHADA DO SUL", "ENCRUZILHADA DO SUL"),
        ("HERVAL", "HERVAL"),
        ("HULHA NEGRA", "HULHA NEGRA"),
        ("JAGUARÃO", "JAGUARÃO"),
        ("LAVRAS DO SUL", "LAVRAS DO SUL"),
        ("MORRO REDONDO", "MORRO REDONDO"),
        ("PEDRAS ALTAS", "PEDRAS ALTAS"),
        ("PEDRO OSÓRIO", "PEDRO OSÓRIO"),
        ("PELOTAS", "PELOTAS"),
        ("JAGUARÃO", "JAGUARÃO"),  # aqui
        ("PINHEIRO MACHADO", "PINHEIRO MACHADO"),
        ("PIRATINI", "PIRATINI"),
        ("RIO GRANDE", "RIO GRANDE"),
        ("SÃO LOURENÇO DO SUL", "SÃO LOURENÇO DO SUL"),
        ("SENTINELA DO SUL", "SENTINELA DO SUL"),
        ("Sertão Santana", "Sertão Santana"),
        ("SANTA VITÓRIA DO PALMAR", "SANTA VITÓRIA DO PALMAR"),
        ("TAPES", "TAPES"),
    ]

    Arvore_investimento = [
        ("Capex", "Capex"),
        ("Opex", "Opex"),
        ("0", "0"),
    ]

    status_sap = [
        ("ABER/ABER", "ABER/ABER"),
        ("LIB/LOG", "LIB/LOG"),
        ("LIB/ATEC", "LIB/ATEC"),
        ("LIB/ENER", "LIB/ENER"),
        ("ENCE/ENCE", "ENCE/ENCE"),
        ("LIB/CKCP", "LIB/CKCP"),
        ("LIB/ENTE", "LIB/ENTE"),
        ("LIB/MED", "LIB/MED"),
        ("LIB/COMS", "LIB/COMS"),
        ("LIB/PEND", "LIB/PEND"),
        ("LIB/CONC", "LIB/CONC"),
        ("LIB/AVAL", "LIB/AVAL"),
        ("LIB/ANTE", "LIB/ANTE"),
        ("LIB/REC", "LIB/REC"),
        ("LIB/DLT", "LIB/DLT"),
        ("LIB/DEV", "LIB/DEV"),
        ("LIB/DFEC", "LIB/DFEC"),
        ("0", "0"),
    ]

    tipo_equipe = [
        ("Linha Morta", "Linha Morta"),
        ("Linha Viva", "Linha Viva"),
        ("Poda", "Poda"),
        ("0", "0"),
    ]

    tipos_de_servicos = [
        ("SUBS DE POSTE", "SUBS DE POSTE"),
        ("SUBS DE TRAFO", "SUBS DE TRAFO"),
        ("SUBS CONDUTOR", "SUBS CONDUTOR"),
        ("APOIO", "APOIO"),
        ("SUBS DE CHAVE FACA", "SUBS DE CHAVE FACA"),
        ("SUBS DE CHAVE FUS", "SUBS DE CHAVE FUS"),
        ("SUBS CONDUTOR", "SUBS CONDUTOR"),
        ("SUBS DE POSTE E TRAFO", "SUBS DE POSTE E TRAFO"),
        ("SUBS DE ESTRUTURA MT", "SUBS DE ESTRUTURA MT"),
        ("CONEXÃO", "CONEXÃO"),
        ("PODA", "PODA"),
        ("CAVA", "CAVA"),
        ("ESPAÇADOR", "ESPAÇADOR"),
        ("TALA", "TALA"),
        ("ELO FUSIVEL", "ELO FUSIVEL"),
        ("RELIGADOR", "RELIGADOR"),
        ("REGULADOR", "REGULADOR"),
        ("MUFLA", "MUFLA"),
        ("RECONDUTORAMENTO DE BT", "RECONDUTORAMENTO DE BT"),
        ("RECONDUTORAMENTO DE MT", "RECONDUTORAMENTO DE MT"),
        ("PODA GRANDE POSTE", "PODA GRANDE POSTE"),
        ("ABATE", "ABATE"),
        ("ESPAÇADOR", "ESPAÇADOR"),
        ("REGULAGEM", "REGULAGEM"),
        ("GLV-CONEXÃO-ARMAÇÃO", "GLV-CONEXÃO-ARMAÇÃO"),
        ("SUBS DE ESTRUTURA BT", "SUBS DE ESTRUTURA BT"),
        ("FLY-TAP", "FLY-TAP"),
        ("ARMAÇÃO E OUTROS", "ARMAÇÃO E OUTROS"),
        ("APRUMO DE POSTE", "APRUMO DE POSTE"),
        ("FECHAMENTO DE CAVA", "FECHAMENTO DE CAVA"),
        ("ELO FUSIVEL", "ELO FUSIVEL"),
        ("ABATE", "ABATE"),
        ("IMPLANTAÇÃO DE POSTE", "IMPLANTAÇÃO DE POSTE"),
        ("IMPLANTAÇÃO DE TRAFO", "IMPLANTAÇÃO DE TRAFO"),
        ("PODA PEQUENO POSTE", "PODA PEQUENO POSTE"),
        ("PODA MENOR DE 5 GALHOS", "PODA MENOR DE 5 GALHOS"),
        ("RETIRAR EQP MEDIÇÃO", "RETIRAR EQP MEDIÇÃO"),
    ]

    Tipo_investimento = models.CharField(
        choices=Arvore_investimento, max_length=50, blank=True, null=True, default=""
    )
    Numero_Servico = models.CharField(
        max_length=100, unique=True, blank=False, null=False
    )
    PEP = models.CharField(max_length=40, unique=True, blank=False, null=False)
    Servico = models.CharField(
        choices=tipo_servico, max_length=50, blank=False, null=False, default=""
    )
    Status_SAP = models.CharField(
        choices=status_sap, max_length=50, blank=True, null=True, default=""
    )
    Equipe = models.ForeignKey(
        Equipe,
        max_length=50,
        blank=True,
        null=True,
        default="",
        on_delete=models.SET_NULL,
    )
    Mês_servico = models.CharField(
        choices=Mes_Mes, max_length=4, blank=False, null=False, default=""
    )
    Ano_servico = models.CharField(max_length=4, blank=False, null=False, default="")
    data_da_solicitacao = models.DateField(blank=False, null=False, default="")
    tipo_servico = models.CharField(
        choices=tipos_de_servicos, max_length=50, blank=False, null=False, default=""
    )
    Status = models.CharField(
        choices=tipo_status, max_length=25, blank=False, null=False, default=""
    )
    Municipio = models.CharField(
        max_length=50, choices=Municipios, blank=False, null=False, default=""
    )
    Endereco = models.CharField(max_length=100, blank=False, null=False)
    data_programacao = models.DateField(blank=True, null=True, default="")
    tecnico = models.CharField(max_length=80, blank=False, null=False, default=False)
    evidencias = models.BooleanField(
        blank=False, null=False, verbose_name="Evidências", default=False
    )
    AES_ACOS = models.BooleanField(blank=False, null=False, default=False)
    As_built = models.BooleanField(blank=False, null=False, default=False)
    Medicao = models.BooleanField(blank=False, null=False, default=False)
    andamento = models.IntegerField(default=0, editable=False)
    Requisicao_ODI = models.BooleanField(blank=False, null=False, default=False)
    Requisicao_ODD = models.BooleanField(blank=False, null=False, default=False)
    Valor_parcial = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    Valor_final = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    Valor_pago = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    desenho_servico = models.FileField(
        upload_to="media/desenhoservico/arquivos/", blank=True, null=True
    )
    foto_antes = models.FileField(
        upload_to="media/desenhoservico/arquivos/", blank=True, null=True
    )
    foto_depois = models.FileField(
        upload_to="media/desenhoservico/arquivos/", blank=True, null=True
    )
    Observacao = models.TextField(max_length=800, blank=True, null=True)

    @staticmethod
    def somar_valor_status(status):
        return (
            Servico.objects.filter(Status=status)
            .aggregate(Sum("Valor_final", default=0))
            .get("Valor_final__sum")
        )

    @staticmethod
    def somar_valor_status_parcial(status):
        return (
            Servico.objects.filter(Status=status)
            .aggregate(Sum("Valor_parcial", default=0))
            .get("Valor_parcial__sum")
        )

    class Meta:
        permissions = [
            ("acesso_servicos", "Acesso ao gestao de servicos"),
        ]

    def get_evidencias_display(self):
        return "Sim" if self.evidencias else "Não"

    def save(self, *args, **kwargs):
        self.andamento = (
            sum([self.evidencias, self.AES_ACOS, self.As_built, self.Medicao]) * 25
        )
        super().save(*args, **kwargs)

