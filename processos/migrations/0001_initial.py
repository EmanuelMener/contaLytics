# Generated by Django 5.1.3 on 2024-12-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('responsavel', models.CharField(max_length=100)),
                ('prazo', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='Em andamento', max_length=50)),
            ],
        ),
    ]
