from django.db import models
from django.core.exceptions import ValidationError

class ProgramacaoEquipes(models.Model):

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

    tipos_de_status_si = [
        ("Autorizado ", "Autorizado "),
        ("Rejeitado", "Rejeitado"),
        ("Pendente ", "Pendente "),
        ("Execução ", "Execução "),
        ("Finalizado", "Finalizado"),
    ]

    turno = [
        ("Dia", "Dia"),
        ("Manhã", "Manhã"),
        ("Tarde", "Tarde"),
        ("Diversos", "Diversos"),
    ]

    SI_OC = models.CharField(max_length=20, blank=False, null=False)
    Nota_PM = models.CharField(max_length=20, blank=True, null=True)
    Ordem_execucao = models.CharField(max_length=20, blank=True, null=True)
    Status_sistema = models.CharField(
        choices=tipos_de_status_si, max_length=50, blank=True, null=True
    )
    Status_campo = models.CharField(max_length=20, blank=True, null=True)
    QTD = models.CharField(max_length=20, blank=True, null=True)
    Prio_DEF = models.CharField(max_length=100, blank=True, null=True)
    Grupo_DEF = models.CharField(max_length=100, blank=True, null=True)
    Alimentador = models.CharField(max_length=20, blank=True, null=True)
    GPS_POSTE = models.CharField(max_length=200, blank=True, null=True)
    linkmaps = models.CharField(max_length=300, blank=True, null=True)
    tipo_servico = models.CharField(
        choices=tipos_de_servicos, max_length=50, blank=True, null=True
    )
    Local = models.CharField(choices=Municipios, max_length=150, blank=True, null=True)
    Endereco = models.CharField(max_length=200, blank=True, null=True)
    tipo_EQP = models.CharField(max_length=300, blank=True, null=True)
    Encarregado = models.CharField(max_length=300, blank=True, null=True)
    dia = models.CharField(max_length=20, blank=True, null=True)
    Mes = models.CharField(max_length=20, blank=True, null=True)
    ANO = models.CharField(max_length=200, blank=True, null=True)
    turno = models.CharField(choices=turno, max_length=8, blank=False, null=False)
    prazo = models.CharField(max_length=200, blank=True, null=True)
    valor_prev = models.CharField(max_length=200, blank=True, null=True)
    valor_final = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.SI_OC

    def clean(self):
        if self.turno != "Diversos":
            if ProgramacaoEquipes.objects.filter(
                Encarregado=self.Encarregado,
                dia=self.dia,
                Mes=self.Mes,
                ANO=self.ANO,
                turno=self.turno,
            ).exists():
                raise ValidationError(
                    "Este encarregado já possui uma tarefa programada para essa data."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProgramacaoEquipes, self).save(*args, **kwargs)
