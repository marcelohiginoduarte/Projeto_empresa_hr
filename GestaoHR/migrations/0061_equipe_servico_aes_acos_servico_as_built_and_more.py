# Generated by Django 5.0.7 on 2024-11-01 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0060_caderno_servico_delete_cadernoservico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_Equipe', models.CharField(max_length=50, unique=True)),
                ('Nome_encarregado', models.CharField(max_length=150)),
                ('Mebro_equipe1', models.CharField(blank=True, max_length=150, null=True)),
                ('Mebro_equipe2', models.CharField(blank=True, max_length=150, null=True)),
                ('Mebro_equipe3', models.CharField(blank=True, max_length=150, null=True)),
                ('Mebro_equipe4', models.CharField(blank=True, max_length=150, null=True)),
                ('Mebro_equipe5', models.CharField(blank=True, max_length=150, null=True)),
                ('Mebro_equipe6', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='AES_ACOS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='As_built',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='Medicao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='Requisicao_ODD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='Requisicao_ODI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='Status_SAP',
            field=models.CharField(blank=True, choices=[('ABER/ABER', 'ABER/ABER'), ('LIB/LOG', 'LIB/LOG'), ('LIB/ATEC', 'LIB/ATEC'), ('LIB/ENER', 'LIB/ENER'), ('ENCE/ENCE', 'ENCE/ENCE'), ('LIB/CKCP', 'LIB/CKCP'), ('LIB/ENTE', 'LIB/ENTE'), ('LIB/MED', 'LIB/MED'), ('LIB/COMS', 'LIB/COMS'), ('LIB/PEND', 'LIB/PEND'), ('LIB/CONC', 'LIB/CONC'), ('LIB/AVAL', 'LIB/AVAL'), ('LIB/ANTE', 'LIB/ANTE'), ('LIB/REC', 'LIB/REC'), ('LIB/DLT', 'LIB/DLT'), ('LIB/DEV', 'LIB/DEV'), ('LIB/DFEC', 'LIB/DFEC'), ('0', '0')], default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='Tipo_investimento',
            field=models.CharField(blank=True, choices=[('Capex', 'Capex'), ('Opex', 'Opex'), ('0', '0')], default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='Valor_pago',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='andamento',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='servico',
            name='evidencias',
            field=models.BooleanField(default=False, verbose_name='Evidências'),
        ),
        migrations.AddField(
            model_name='servico',
            name='tecnico',
            field=models.CharField(default=False, max_length=80),
        ),
        migrations.AddField(
            model_name='servico',
            name='tipo_servico',
            field=models.CharField(choices=[('REGULAGEM', 'REGULAGEM'), ('GLV-CONEXÃO-ARMAÇÃO', 'GLV-CONEXÃO-ARMAÇÃO'), ('SUBS DE ESTRUTURA BT', 'SUBS DE ESTRUTURA BT'), ('FLY-TAP', 'FLY-TAP'), ('ARMAÇÃO E OUTROS', 'ARMAÇÃO E OUTROS'), ('APRUMO DE POSTE', 'APRUMO DE POSTE'), ('FECHAMENTO DE CAVA', 'FECHAMENTO DE CAVA'), ('ELO FUSIVEL', 'ELO FUSIVEL'), ('ABATE', 'ABATE'), ('IMPLANTAÇÃO DE POSTE', 'IMPLANTAÇÃO DE POSTE'), ('IMPLANTAÇÃO DE TRAFO', 'IMPLANTAÇÃO DE TRAFO'), ('PODA PEQUENO POSTE', 'PODA PEQUENO POSTE'), ('PODA MENOR DE 5 GALHOS', 'PODA MENOR DE 5 GALHOS'), ('RETIRAR EQP MEDIÇÃO', 'RETIRAR EQP MEDIÇÃO'), ('0', '0')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='servico',
            name='Equipe',
            field=models.ForeignKey(blank=True, default='', max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GestaoHR.equipe'),
        ),
    ]
