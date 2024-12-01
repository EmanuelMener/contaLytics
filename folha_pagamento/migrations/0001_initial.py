# Generated by Django 5.1.3 on 2024-12-01 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='FolhaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.DateField()),
                ('horas_extras', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('descontos', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('salario_liquido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folha_pagamento.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroPonto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folha_pagamento.funcionario')),
            ],
        ),
    ]
