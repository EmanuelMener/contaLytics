# Generated by Django 5.1.3 on 2024-12-01 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folha_pagamento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='salario_base',
            new_name='salario',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_saida', models.TimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folha_pagamento.funcionario')),
            ],
        ),
        migrations.DeleteModel(
            name='RegistroPonto',
        ),
    ]
