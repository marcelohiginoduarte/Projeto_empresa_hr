from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from GestaoHR.models import collaborator


@shared_task
def verificar_vencimento_ferias():
    hoje = timezone.now().date()
    proximos_dias = hoje + timedelta(days=30)
    funcionarios = collaborator.objects.filter(Data_ferias__range=(hoje, proximos_dias))

    if funcionarios:
        enviar_email_alerta(funcionarios)

def enviar_email_alerta(funcionarios):
    assunto = 'Alerta: Férias Próximas'

    mensagem = 'Os seguintes funcionários tês férias próximas: \n\n'
    for funcionario in funcionarios:
        mensagem += f'{funcionario.Nome}: {funcionario.Data_ferias}\n'

    mensagem += '\nPor favor, tome as providências.'

    destinatarios = 'marcelihigino@gmail.com'



    send_mail(
        assunto,
        mensagem,
        '',
        destinatarios
    )
