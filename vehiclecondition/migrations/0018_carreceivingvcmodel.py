# Generated by Django 5.0.4 on 2024-04-08 21:34

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0017_alter_vehicleconditionmodel_proof_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarReceivingVCModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wo_number', models.CharField(max_length=25, verbose_name='WO')),
                ('receiving_from', models.CharField(blank=True, max_length=50, null=True, verbose_name='Receiving From VC Form')),
                ('date_and_time', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Date and Time')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Location')),
                ('signature', models.CharField(blank=True, max_length=50, null=True, verbose_name='Signature')),
                ('vehicle_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiclecondition.vehicleconditionmodel')),
            ],
        ),
    ]
