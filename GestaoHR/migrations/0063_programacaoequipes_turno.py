# Generated by Django 5.0.7 on 2024-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoHR', '0062_programacaoequipes_alter_servico_tipo_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacaoequipes',
            name='turno',
            field=models.CharField(choices=[('Dia', 'Dia'), ('Manhã', 'Manhã'), ('Tarde', 'Tarde')], default='dia', max_length=8),
            preserve_default=False,
        ),
    ]
