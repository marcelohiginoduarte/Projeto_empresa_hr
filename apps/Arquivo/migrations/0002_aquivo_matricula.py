# Generated by Django 5.0.7 on 2025-01-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Arquivo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aquivo",
            name="matricula",
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
