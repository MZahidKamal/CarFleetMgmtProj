# Generated by Django 5.0.4 on 2024-04-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0010_alter_vehicleconditionmodel_fuel_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleconditionmodel',
            name='fuel_level',
            field=models.CharField(choices=[('0/10', '0/10'), ('1/10', '1/10'), ('2/10', '2/10'), ('3/10', '3/10'), ('4/10', '4/10'), ('5/10', '5/10'), ('6/10', '6/10'), ('7/10', '7/10'), ('8/10', '8/10'), ('9/10', '9/10'), ('10/10', '10/10')], default='0/10', max_length=10, verbose_name='Fuel Level'),
        ),
    ]