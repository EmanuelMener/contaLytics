# Generated by Django 5.1.3 on 2024-12-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='id',
        ),
        migrations.AddField(
            model_name='processo',
            name='protocolo',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
