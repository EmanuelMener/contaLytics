# Generated by Django 5.1.3 on 2024-12-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folha_pagamento', '0002_rename_salario_base_funcionario_salario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folhapagamento',
            old_name='salario_liquido',
            new_name='total',
        ),
        migrations.RemoveField(
            model_name='folhapagamento',
            name='descontos',
        ),
        migrations.RemoveField(
            model_name='folhapagamento',
            name='horas_extras',
        ),
        migrations.AddField(
            model_name='folhapagamento',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folhapagamento',
            name='mes',
            field=models.CharField(max_length=7),
        ),
    ]
