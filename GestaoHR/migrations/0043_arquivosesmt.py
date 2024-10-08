# Generated by Django 5.0.7 on 2024-09-13 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0042_rename_brigada_emergencia_sesmt_brigada_emergerncia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoSesmt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('arquivo', models.FileField(upload_to='media/sesmt/sesmt_t')),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('versao_anterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='versoes', to='GestaoHR.arquivosesmt')),
            ],
        ),
    ]
