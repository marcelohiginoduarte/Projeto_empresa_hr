# Generated by Django 5.0.7 on 2024-09-24 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0047_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField(default=0)),
                ('categoria', models.CharField(choices=[('EPI', 'EPI'), ('EPC', 'EPC')], max_length=50)),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('data_entrada', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovimentacaoEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ENTRADA', 'Entrada'), ('SAIDA', 'Saída')], max_length=7)),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestaoHR.produto')),
            ],
        ),
    ]