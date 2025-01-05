from django.db import models
from Equipe.models import Equipe

class FotosCampo(models.Model):

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

    projeto = models.CharField(max_length=15, null=False, blank=False)
    poste = models.CharField(max_length=4, null=False, blank=False)
    Poste_antes = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Poste_depois = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    cava_antes = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    cava_depois = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    GPS_antes = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    GPS_depois = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Estrutura_antes = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Estrutura_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    panoramica = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Equipamento_antes = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Equipamento_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_serie_antes = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_serie_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_sap_antes = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_sap_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_placa_antes = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Numero_placa_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Poda_antes = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Poda_depois = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    concreto_calcada_antes = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    concreto_calcada_depois = models.ImageField(
        upload_to="fotos/campos", blank=True, null=True
    )
    Tela_Ocorencia = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Trajeto = models.ImageField(upload_to="fotos/campos", blank=True, null=True)
    Data = models.DateField(blank=True, null=True)
    Supervisor = models.CharField(max_length=25, blank=False, null=False)
    Equipe = models.ForeignKey(Equipe, on_delete=models.SET_DEFAULT, default=1)
    Cidade = models.CharField(
        choices=Municipios, max_length=100, blank=False, null=False
    )
    Endereco = models.CharField(max_length=300, blank=False, null=False)
    ocorrencia = models.CharField(max_length=20, blank=False, null=False)
    GPS = models.CharField(max_length=20, blank=False, null=False)
    servico = models.CharField(max_length=300, blank=False, null=False)
    horario_inicio = models.TimeField(blank=False, null=False)
    horario_fim = models.TimeField(blank=True, null=True)

    class Meta:
        permissions = [
            ("acesso_fotoscampo", "Acesso as fotos de campo"),
        ]

class arquivos_foto(models.Model):
    projeto = models.CharField(max_length=25, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.projeto
