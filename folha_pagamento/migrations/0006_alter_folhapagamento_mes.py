# Generated by Django 5.1.3 on 2024-12-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folha_pagamento', '0005_alter_folhapagamento_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folhapagamento',
            name='mes',
            field=models.DateField(blank=True, null=True),
        ),
    ]