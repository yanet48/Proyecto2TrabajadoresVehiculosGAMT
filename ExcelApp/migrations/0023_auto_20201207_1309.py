# Generated by Django 3.1.1 on 2020-12-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelApp', '0022_conductor_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placa',
            name='placa1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='placa',
            name='placa2',
            field=models.CharField(max_length=100),
        ),
    ]
