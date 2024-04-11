# Generated by Django 5.0.4 on 2024-04-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0003_alter_vehicleconditionmodel_fuel_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleconditionmodel',
            name='fuel_level',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='OPTION_ZERO', verbose_name='Fuel Level'),
        ),
    ]