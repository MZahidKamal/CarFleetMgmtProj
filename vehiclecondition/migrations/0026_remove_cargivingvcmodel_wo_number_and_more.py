# Generated by Django 5.0.4 on 2024-04-13 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0025_alter_carreceivingvcmodel_wo_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargivingvcmodel',
            name='wo_number',
        ),
        migrations.RemoveField(
            model_name='carreceivingvcmodel',
            name='wo_number',
        ),
    ]