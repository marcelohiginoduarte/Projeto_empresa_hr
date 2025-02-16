from django.db import migrations
from datetime import datetime
from django.db import models

def fix_invalid_dates(apps, schema_editor):
    Demandainterna = apps.get_model('GestaoHR', 'Demandainterna')
    # Atualiza registros com data_solicitacao nula ou vazia com a data e hora atual
    Demandainterna.objects.filter(data_solicitacao__isnull=True).update(data_solicitacao=datetime.now())
    # Ajustar para filtrar onde a data_solicitacao está vazia ou nula
    Demandainterna.objects.filter(data_solicitacao=None).update(data_solicitacao=datetime.now())

from django.db import migrations, models
from datetime import datetime

def fix_invalid_dates(apps, schema_editor):
    # Se a coluna 'data_solicitacao' não existir mais, podemos remover essa função
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0034_demandainterna_observacao_and_more'),
    ]

    operations = [
        # Remover a operação que alterava o campo 'data_solicitacao', já que ele foi removido.
        migrations.RunPython(fix_invalid_dates),  # Não há mais necessidade de corrigir data_solicitacao
        migrations.AlterField(
            model_name='collaborator',
            name='Servico',
            field=models.CharField(choices=[('Administrativo', 'Administrativo'), ('Operacional', 'Operacional')], max_length=20),
        ),
    ]


