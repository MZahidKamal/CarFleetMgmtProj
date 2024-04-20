# Generated by Django 5.0.4 on 2024-04-20 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
        ('workorder', '0008_alter_workordersmodel_car_dealer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workordersmodel',
            name='car_vin',
        ),
        migrations.AddField(
            model_name='workordersmodel',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.carmodel', verbose_name='Car'),
        ),
    ]
