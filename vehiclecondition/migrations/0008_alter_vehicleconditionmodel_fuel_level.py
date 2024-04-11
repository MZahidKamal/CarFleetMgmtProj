# Generated by Django 5.0.4 on 2024-04-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0007_alter_proofimagesmodel_vin_number_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleconditionmodel',
            name='fuel_level',
            field=models.IntegerField(choices=[('OPTION_ONE', 1), ('OPTION_TWO', 2)], default='OPTION_ZERO', verbose_name='Fuel Level'),
        ),
    ]
