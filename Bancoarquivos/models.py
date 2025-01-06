from django.db import models


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
