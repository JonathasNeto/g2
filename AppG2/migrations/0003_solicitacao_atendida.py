# Generated by Django 2.0.13 on 2019-12-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppG2', '0002_auto_20191207_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='atendida',
            field=models.BooleanField(default=False),
        ),
    ]
