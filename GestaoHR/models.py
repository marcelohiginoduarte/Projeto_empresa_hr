from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Sum


class collaborator(models.Model):
    tipo_servico = [
        ('Administrativo','Administrativo'),
        ('Externo', 'Externo'),
    ]
    Nome = models.CharField(max_length=150, blank=False, null=False)
    CPF = models.CharField(max_length=11, unique=True, blank=False, null=False)
    RG = models.CharField(max_length=12, unique=True, blank=True, null=True)
    Servico = models.CharField(max_length=20,choices=tipo_servico, )
    CNH = models.CharField(max_length=12, blank=True, null=True)
    Vencimento_CNH = models.DateField(blank=True, null=True)
    Data_contratacao = models.DateField(blank=True, null=True)
    Data_ferias = models.DateField()
    matricula = models.CharField(max_length=15, blank=True, null=True, unique=True)
    ASO = models.FileField(upload_to='media/ASO/', blank=True, null=True)
    validade_aso = models.DateField()
    PIS = models.CharField(max_length=15, blank=True, null=True)
    Salario = models.DecimalField(max_digits=10, decimal_places=2, )
    Controle_folha_ponto = models.FileField(upload_to='media/Controle_folha_ponto/', blank=True, null=True)
    Seguro_de_vida = models.FileField(upload_to='media/Seguro_vida/', blank=True, null=True)


    def calcular_data_ferias(self):
        data_ferias=self.Data_contratacao + timedelta(days=365)
        return data_ferias

    def save(self, *args,**kwargs):
        self.Data_ferias = self.calcular_data_ferias()
        super().save(*args, **kwargs)

    def datafutura(self):
        super().clean()
        if self.Vencimento_CNH < timezone.now().date():
            raise ValidationError('A data deve ser uma data futura')


    def __str__(self):
        return self.Nome
    

class Aquivo(models.Model):
    Mes_Mes=[
        ('Jan','Jan'),
        ('Fev','Fev'),
        ('Mar','Mar'),
        ('Abr','Abr'),
        ('Mai','Mai'),
        ('Jun','Jun'),
        ('Jul','Jul'),
        ('Ago','Ago'),
        ('Set','Set'),
        ('Out','Out'),
        ('Nov','Nov'),
        ('Dez','Dez'),
    ]
    Nome = models.ForeignKey(collaborator, on_delete=models.CASCADE, related_name='arquivos_mensal')
    Arquivo_ponto = models.FileField(upload_to='media/imagens/Controle_folha_ponto/')
    Mes = models.CharField(max_length=6, choices=Mes_Mes, blank=False, null=False)
    Ano = models.IntegerField(default=datetime.now().year)
    

class Servico(models.Model):
    tipo_servico=[
        ('Plano de Manutenção','Plano de Manutenção'),
        ('Desenho tecnico','Desenho tecnico'),
        ('Ocorrência','Ocorrência'),
    ]
    tipo_status = [
        ('Programação','Programação'),
        ('Andamento','Andamento'),
        ('Espera','Espera'),
        ('Concluido','Concluido'),
        ('Fechamento','Fechamento'),
        ('Pagamento','Pagamento'),
        ('Recebido','Recebido'),
    ]

    Mes_Mes=[
        ('Jan','Jan'),
        ('Fev','Fev'),
        ('Mar','Mar'),
        ('Abr','Abr'),
        ('Mai','Mai'),
        ('Jun','Jun'),
        ('Jul','Jul'),
        ('Ago','Ago'),
        ('Set','Set'),
        ('Out','Out'),
        ('Nov','Nov'),
        ('Dez','Dez'),
    ]

    Municipios = [
        ('ALVORADA','ALVORADA'),
        ('ARROIO DOS RATOS','ARROIO DOS RATOS'),
        ('BARRA DO RIBEIRO','BARRA DO RIBEIRO'),
        ('BUTIÁ','BUTIÁ'),
        ('CHARQUEADAS','CHARQUEADAS'),
        ('ELDORADO DO SUL','ELDORADO DO SUL'),
        ('GUAÍBA','GUAÍBA'),
        ('MARIANA PIMENTEL','MARIANA PIMENTEL'),
        ('MINAS DO LEÃO','MINAS DO LEÃO'),
        ('PANTANO GRANDE','PANTANO GRANDE'),
        ('PORTO ALEGRE','PORTO ALEGRE'),
        ('SÃO JERÔNIMO','SÃO JERÔNIMO'),
        ('VIAMÃO','VIAMÃO'),
        ('AMARAL FERRADOR','AMARAL FERRADOR'), 
        ('ARAMBARÉ','ARAMBARÉ'),
        ('ARROIO DO PADRE','ARROIO DO PADRE'),
        ('ARROIO GRANDE','ARROIO GRANDE'),
        ('BAGÉ','BAGÉ'),
        ('BARAO DO TRIUNFO','BARAO DO TRIUNFO'),
        ('CAMAQUÃ','CAMAQUÃ'),
        ('CANDIOTA','CANDIOTA'),
        ('CANGUÇU','CANGUÇU'),
        ('CAPÃO DO LEÃO','CAPÃO DO LEÃO'),
        ('CERRITO','CERRITO'),
        ('CERRO GRANDE DO SUL','CERRO GRANDE DO SUL'),
        ('CHUÍ','CHUÍ'),
        ('CHUVISCA','CHUVISCA'),
        ('CRISTAL','CRISTAL'),
        ('DOM FELICIANO','BDOM FELICIANO'),
        ('DOM PEDRITO','DOM PEDRITO'),
        ('ENCRUZILHADA DO SUL','ENCRUZILHADA DO SUL'),
        ('HERVAL','HERVAL'),
        ('HULHA NEGRA','HULHA NEGRA'),
        ('JAGUARÃO','JAGUARÃO'),
        ('LAVRAS DO SUL','LAVRAS DO SUL'),
        ('MORRO REDONDO','MORRO REDONDO'),
        ('PEDRAS ALTAS','PEDRAS ALTAS'),
        ('PEDRO OSÓRIO','PEDRO OSÓRIO'),
        ('PELOTAS','PELOTAS'),
        ('JAGUARÃO','JAGUARÃO'),#aqui
        ('PINHEIRO MACHADO','PINHEIRO MACHADO'),
        ('PIRATINI','PIRATINI'),
        ('RIO GRANDE','RIO GRANDE'),
        ('SÃO LOURENÇO DO SUL','SÃO LOURENÇO DO SUL'),
        ('SENTINELA DO SUL','SENTINELA DO SUL'),
        ('Sertão Santana','Sertão Santana'),
        ('SANTA VITÓRIA DO PALMAR','SANTA VITÓRIA DO PALMAR'),
        ('TAPES','TAPES'),
    ]

    Numero_Servico = models.CharField(max_length=100, unique=True ,blank=False, null=False)
    PEP = models.IntegerField(unique=True, blank=False, null=False)
    Servico = models.CharField(choices=tipo_servico, max_length=50, blank=False, null=False)
    Mês_servico = models.CharField(choices=Mes_Mes,max_length=4, blank=False, null=False)
    Ano_servico = models.CharField(max_length=4,blank=False, null=False)
    data_da_solicitacao = models.DateField(blank=False, null=False)
    Status = models.CharField(choices=tipo_status, max_length=25, blank=False, null=False)
    Municipio = models.CharField(max_length=50,choices=Municipios, blank=False, null=False)
    Endereco = models.CharField(max_length=100, blank=False, null=False)
    data_programacao = models.DateField(blank=True, null=True)
    Valor_parcial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Valor_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desenho_servico = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    foto_antes = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    foto_depois = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    Observacao = models.TextField(max_length=200, blank=True, null=True)

    @staticmethod
    def somar_valor_status(status):
        return Servico.objects.filter(Status=status).aggregate(Sum('Valor_final',default=0)).get('Valor_final__sum')
        
        

class DemandaInterna(models.Model):
    tipo_atividade= [
        ('Desenho','Desenho'),
        ('Medição', 'Medição'),
        ('Verificar campo', 'Verificar Campo'),
        ('Documentação', 'Documentação')
    ]

    tipo_status = [
        ('Aguardando', 'Aguardando'),
        ('Andamento', 'Andamento'),
        ('Realizando', 'Realizado'),
        ('Correção', 'Correção'),
    ]

    Atividade = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(max_length=50, choices=tipo_atividade, blank=False, null=False)
    responsavel = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=30,choices=tipo_status, blank=False, null=False)
    data_solicitacao = models.DateField(blank=True, null=True)
    data_conclusão= models.DateField(blank=True, null=True)
    responsavel = models.CharField(max_length=50, blank=True, null=True)
    arquivos = models.FileField(upload_to='media/desenhoservico/Interna/', blank=True, null=True)
    arquivos_complementar = models.FileField(upload_to='media/desenhoservico/Interna/', blank=True, null=True)
    arquivos_complementar1 = models.FileField(upload_to='media/desenhoservico/Interna/', blank=True, null=True)
    arquivos_complementar2 = models.FileField(upload_to='media/desenhoservico/Interna/', blank=True, null=True)

class BancoArquivos(models.Model):

    tipo_servico=[
        ('Plano de Manutenção','Plano de Manutenção'),
        ('Desenho tecnico','Desenho tecnico'),
        ('Ocorrência','Ocorrência'),
    ]

    Municipios = [
        ('ALVORADA','ALVORADA'),
        ('ARROIO DOS RATOS','ARROIO DOS RATOS'),
        ('BARRA DO RIBEIRO','BARRA DO RIBEIRO'),
        ('BUTIÁ','BUTIÁ'),
        ('CHARQUEADAS','CHARQUEADAS'),
        ('ELDORADO DO SUL','ELDORADO DO SUL'),
        ('GUAÍBA','GUAÍBA'),
        ('MARIANA PIMENTEL','MARIANA PIMENTEL'),
        ('MINAS DO LEÃO','MINAS DO LEÃO'),
        ('PANTANO GRANDE','PANTANO GRANDE'),
        ('PORTO ALEGRE','PORTO ALEGRE'),
        ('SÃO JERÔNIMO','SÃO JERÔNIMO'),
        ('VIAMÃO','VIAMÃO'),
        ('AMARAL FERRADOR','AMARAL FERRADOR'), 
        ('ARAMBARÉ','ARAMBARÉ'),
        ('ARROIO DO PADRE','ARROIO DO PADRE'),
        ('ARROIO GRANDE','ARROIO GRANDE'),
        ('BAGÉ','BAGÉ'),
        ('BARAO DO TRIUNFO','BARAO DO TRIUNFO'),
        ('CAMAQUÃ','CAMAQUÃ'),
        ('CANDIOTA','CANDIOTA'),
        ('CANGUÇU','CANGUÇU'),
        ('CAPÃO DO LEÃO','CAPÃO DO LEÃO'),
        ('CERRITO','CERRITO'),
        ('CERRO GRANDE DO SUL','CERRO GRANDE DO SUL'),
        ('CHUÍ','CHUÍ'),
        ('CHUVISCA','CHUVISCA'),
        ('CRISTAL','CRISTAL'),
        ('DOM FELICIANO','BDOM FELICIANO'),
        ('DOM PEDRITO','DOM PEDRITO'),
        ('ENCRUZILHADA DO SUL','ENCRUZILHADA DO SUL'),
        ('HERVAL','HERVAL'),
        ('HULHA NEGRA','HULHA NEGRA'),
        ('JAGUARÃO','JAGUARÃO'),
        ('LAVRAS DO SUL','LAVRAS DO SUL'),
        ('MORRO REDONDO','MORRO REDONDO'),
        ('PEDRAS ALTAS','PEDRAS ALTAS'),
        ('PEDRO OSÓRIO','PEDRO OSÓRIO'),
        ('PELOTAS','PELOTAS'),
        ('JAGUARÃO','JAGUARÃO'),#aqui
        ('PINHEIRO MACHADO','PINHEIRO MACHADO'),
        ('PIRATINI','PIRATINI'),
        ('RIO GRANDE','RIO GRANDE'),
        ('SÃO LOURENÇO DO SUL','SÃO LOURENÇO DO SUL'),
        ('SENTINELA DO SUL','SENTINELA DO SUL'),
        ('Sertão Santana','Sertão Santana'),
        ('SANTA VITÓRIA DO PALMAR','SANTA VITÓRIA DO PALMAR'),
        ('TAPES','TAPES'),
    ]
        
    EI_OC = models.CharField(max_length=100, unique=True, blank=False, null=False)
    tipo = models.CharField(max_length=50, choices=tipo_servico, blank=False, null=False)
    municipio = models.CharField(max_length=50, choices=Municipios ,  blank=False, null=False)
    Responsavel = models.CharField(max_length=50, blank=False, null=False)
    AS_Biult = models.FileField(upload_to='media/desenhoservico/Arquivos/', blank=False, null=False)
    Medicao = models.FileField(upload_to='media/desenhoservico/Arquivos/', blank=True, null=True)
    DWG = models.FileField(upload_to='media/desenhoservico/Arquivos/', blank=True, null=True)
    AES = models.FileField(upload_to='media/desenhoservico/Arquivos/', blank=True, null=True)
    ACOS = models.FileField(upload_to='media/desenhoservico/Arquivos/', blank=True, null=True)