# Generated by Django 5.0.7 on 2024-08-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0005_collaborator_data_ferias_alter_collaborator_salario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='ASO',
            field=models.FileField(blank=True, null=True, upload_to='GestaoHR/imagens/ASO/'),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='Controle_folha_ponto',
            field=models.FileField(blank=True, null=True, upload_to='GestaoHR/imagens/Controle_folha_ponto/'),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='Seguro_de_vida',
            field=models.FileField(blank=True, null=True, upload_to='GestaoHR/imagens/Seguro_vida/'),
        ),
    ]
