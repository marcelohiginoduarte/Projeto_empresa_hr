# Generated by Django 5.0.7 on 2024-08-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0025_bancoarquivos_medicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancoarquivos',
            name='EI_OC',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
