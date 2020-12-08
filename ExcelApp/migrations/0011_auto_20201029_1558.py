# Generated by Django 3.1.1 on 2020-10-29 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelApp', '0010_auto_20201029_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa1', models.CharField(max_length=20)),
                ('placa2', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'placa',
            },
        ),
        migrations.RemoveField(
            model_name='programaciongeneral',
            name='placa1',
        ),
        migrations.RemoveField(
            model_name='programaciongeneral',
            name='placa2',
        ),
        migrations.RemoveField(
            model_name='programaciongeneral',
            name='relevo_placa1',
        ),
        migrations.RemoveField(
            model_name='programaciongeneral',
            name='relevo_placa2',
        ),
        migrations.AddField(
            model_name='programaciongeneral',
            name='conductor_placa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='conductor_placa', to='ExcelApp.placa'),
        ),
        migrations.AddField(
            model_name='programaciongeneral',
            name='conductor_relevo_placa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='conductor_relevo_placa', to='ExcelApp.placa'),
        ),
    ]
