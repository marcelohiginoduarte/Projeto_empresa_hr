from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("GestaoHR", "0069_alter_bancoarquivos_ei_oc_alter_collaborator_cpf_and_more"),
    ]

    operations = [
        # Passo 1: Reverter o campo 'id' para o tipo AutoField (campo de chave primária padrão)
        migrations.AlterField(
            model_name="document",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),

        # Passo 2: Restaurar a restrição de unique_together, se necessário
        migrations.AlterUniqueTogether(
            name="document",
            unique_together={("file", "version")},
        ),

        # Passo 3: Adicionar a restrição de unicidade para (file, version)
        migrations.AddConstraint(
            model_name="document",
            constraint=models.UniqueConstraint(
                fields=("file", "version"), name="unique_file_version"
            ),
        ),
    ]


