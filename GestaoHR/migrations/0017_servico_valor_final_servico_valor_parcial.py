# Generated by Django 5.0.7 on 2024-08-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0016_rename_ei_servico_pep'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='Valor_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='Valor_parcial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
