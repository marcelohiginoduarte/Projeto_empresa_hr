# Generated by Django 5.0.7 on 2024-10-10 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0051_alter_fotoscampo_equipamento_antes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborator',
            options={'permissions': [('acesso_rh', 'Acesso ao departamento de RH')]},
        ),
    ]
