from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone



class collaborator(models.Model):
    tipo_servico = [
        ("Administrativo", "Administrativo"),
        ("Operacional", "Operacional"),
    ]
    Nome = models.CharField(max_length=150, blank=False, null=False)
    CPF = models.CharField(max_length=22, unique=False, blank=False, null=False)
    RG = models.CharField(max_length=12, unique=False, blank=True, null=True)
    Servico = models.CharField(max_length=20, choices=tipo_servico)
    CNH = models.CharField(max_length=12, blank=True, null=True)
    Vencimento_CNH = models.DateField(blank=True, null=True)
    Data_contratacao = models.DateField(blank=True, null=True)
    Data_ferias = models.DateField()
    matricula = models.CharField(max_length=15, blank=True, null=True, unique=True)
    ASO = models.FileField(upload_to="media/ASO/", blank=True, null=True)
    validade_aso = models.DateField()
    PIS = models.CharField(max_length=15, blank=True, null=True)
    Salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    Controle_folha_ponto = models.FileField(
        upload_to="media/Controle_folha_ponto/", blank=True, null=True
    )
    Seguro_de_vida = models.FileField(
        upload_to="media/Seguro_vida/", blank=True, null=True
    )

    def calcular_data_ferias(self):
        data_ferias = self.Data_contratacao + timedelta(days=365)
        return data_ferias

    def save(self, *args, **kwargs):
        self.Data_ferias = self.calcular_data_ferias()
        super().save(*args, **kwargs)

    def datafutura(self):
        super().clean()
        if self.Vencimento_CNH < timezone.now().date():
            raise ValidationError("A data deve ser uma data futura")

    def __str__(self):
        return self.Nome

    class Meta:
        permissions = [
            ("acesso_rh", "Acesso ao departamento de RH"),
        ]


class BancoArquivos(models.Model):

    tipo_servico = [
        ("Plano de Manutenção", "Plano de Manutenção"),
        ("Desenho tecnico", "Desenho tecnico"),
        ("Ocorrência", "Ocorrência"),
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

    EI_OC = models.CharField(max_length=100, unique=False, blank=False, null=False)
    tipo = models.CharField(
        max_length=50, choices=tipo_servico, blank=False, null=False
    )
    municipio = models.CharField(
        max_length=50, choices=Municipios, blank=False, null=False
    )
    Responsavel = models.CharField(max_length=50, blank=False, null=False)
    AS_Biult = models.FileField(
        upload_to="media/desenhoservico/Arquivos/", blank=False, null=False
    )
    Medicao = models.FileField(
        upload_to="media/desenhoservico/Arquivos/", blank=True, null=True
    )
    DWG = models.FileField(
        upload_to="media/desenhoservico/Arquivos/", blank=True, null=True
    )
    AES = models.FileField(
        upload_to="media/desenhoservico/Arquivos/", blank=True, null=True
    )
    ACOS = models.FileField(
        upload_to="media/desenhoservico/Arquivos/", blank=True, null=True
    )

    class Meta:
        permissions = [
            ("acesso_demandaInterna", "Acesso ao gestao de demandainterna"),
        ]


class arquivos_foto(models.Model):
    projeto = models.CharField(max_length=25, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.projeto


class Caderno_servico(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to="media/cadernoservico/")

    def __str__(self):
        return self.nome


class AES_ACOS(models.Model):
    aes = models.FileField(upload_to="media/aes", blank=True, null=True)
    acos = models.FileField(upload_to="media/acos", blank=True, null=True)


class ItemServico(models.Model):
    iten = models.CharField(max_length=3)
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    QTD = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
