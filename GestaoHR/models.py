from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Sum


class collaborator(models.Model):
    tipo_servico = [
        ('Administrativo','Administrativo'),
        ('Operacional', 'Operacional'),
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
    PEP = models.CharField(max_length=40, unique=True, blank=False, null=False)
    Servico = models.CharField(choices=tipo_servico, max_length=50, blank=False, null=False, default='')
    Mês_servico = models.CharField(choices=Mes_Mes,max_length=4, blank=False, null=False, default='')
    Ano_servico = models.CharField(max_length=4,blank=False, null=False, default='')
    data_da_solicitacao = models.DateField(blank=False, null=False, default='')
    Status = models.CharField(choices=tipo_status, max_length=25, blank=False, null=False, default='')
    Municipio = models.CharField(max_length=50,choices=Municipios, blank=False, null=False, default='')
    Endereco = models.CharField(max_length=100, blank=False, null=False)
    data_programacao = models.DateField(blank=True, null=True, default='')
    Valor_parcial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Valor_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    desenho_servico = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    foto_antes = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    foto_depois = models.FileField(upload_to='media/desenhoservico/arquivos/', blank=True, null=True)
    Observacao = models.TextField(max_length=200, blank=True, null=True)

    @staticmethod
    def somar_valor_status(status):
        return Servico.objects.filter(Status=status).aggregate(Sum('Valor_final',default=0)).get('Valor_final__sum')
    
    @staticmethod
    def somar_valor_status_parcial(status):
        return Servico.objects.filter(Status=status).aggregate(Sum('Valor_parcial',default=0)).get('Valor_parcial__sum')
        
        

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
        ('Realizado', 'Realizado'),
        ('Correção', 'Correção'),
        ('Enviado Equatorial', 'Enviado Equatorial'),
        ('Aprovado Equatorial', 'Aprovado Equatorial'),
        ('Correção Equatorial', 'Correção Equatorial'),
    ]

    Atividade = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(max_length=50, choices=tipo_atividade, blank=False, null=False)
    responsavel = models.CharField(max_length=50, blank=True, null=True, default='')
    status = models.CharField(max_length=30,choices=tipo_status, blank=False, null=False)
    data_solicitacao = models.DateField(blank=True, null=True )
    data_conclusão= models.DateField(blank=True, null=True)
    responsavel_demanda = models.CharField(max_length=50, blank=True, null=True, default='')
    Observacao = models.TextField(max_length=200, blank=True, null=True)
    arquivos  = models.FileField(upload_to='media/desenhoservico/Interna/', blank=True, null=True)
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


class arquivos_foto(models.Model):
    projeto = models.CharField(max_length=25, null=False, blank=False)

class FotosCampo(models.Model):
    projeto = models.ForeignKey(arquivos_foto, on_delete=models.CASCADE, related_name='fotos')
    Poste_antes= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    Poste_depois = models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    cava_antes= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    cava_depois= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    GPS_antes= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    GPS_depois= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    Estrutura_antes= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    Estrutura_depois= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    panoramica = models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    Equipamento_antes= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    Equipamento_depois= models.ImageField(upload_to='media/fotos/campos', blank=True, null=True)
    
    def __str__(self):
        return self.GPS_antes or 'Foto sem arquivo'

class SESMT (models.Model):
    Brigada_emergerncia = models.FileField(upload_to='media/sesmt/brigada', blank=True, null=True)    
    CIPA = models.FileField(upload_to='media/sesmt/cipa', blank=True, null=True)
    CNPJ_CRB = models.FileField(upload_to='media/sesmt/cnpj', blank=True, null=True)
    CRB = models.FileField(upload_to='media/sesmt/crb', blank=True, null=True)
    Documentacao_veiculo = models.FileField(upload_to='media/sesmt/documentoveiculo', blank=True, null=True)
    manual_veiculo = models.FileField(upload_to='media/sesmt/manual', blank=True, null=True)
    orcamentos = models.FileField(upload_to='media/sesmt/orcamento', blank=True, null=True)
    PCSMO = models.FileField(upload_to='media/sesmt/pcsmo', blank=True, null=True)
    prg = models.FileField(upload_to='media/sesmt/prg', blank=True, null=True)
    plano_de_atendimento_emergencia = models.FileField(upload_to='media/sesmt/planodeatendimento', blank=True, null=True)
    plano_de_manutencao_frota = models.FileField(upload_to='media/sesmt/plfrota', blank=True, null=True)
    POP_lM_construcao = models.FileField(upload_to='media/sesmt/POPLMCONST', blank=True, null=True)
    POP_LV_contrucao = models.FileField(upload_to='media/sesmt/POPLVCONST', blank=True, null=True)
    POP_sesmt = models.FileField(upload_to='media/sesmt/POPSESMT', blank=True, null=True)
    PPCI = models.FileField(upload_to='media/sesmt/PPCI', blank=True, null=True)
    SESMT_t = models.FileField(upload_to='media/sesmt/sesmt_t', blank=True, null=True)
    Ultima_atualização = models.CharField(max_length=50)

class ArquivoSesmt(models.Model):
    Nome = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='media/sesmt/sesmt_t')
    data_envio= models.DateTimeField(auto_now_add=True)
    versao_anterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='versoes')

    def __str__(self):
        return self.Nome

