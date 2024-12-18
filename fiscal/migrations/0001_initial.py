# Generated by Django 5.1.3 on 2024-12-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=7)),
                ('rbt12', models.DecimalField(decimal_places=2, max_digits=12)),
                ('faturamento_base_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('aliquota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imposto_devido', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
