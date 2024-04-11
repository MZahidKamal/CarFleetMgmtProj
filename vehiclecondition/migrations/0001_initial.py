# Generated by Django 5.0.4 on 2024-04-08 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProofImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_number_image', models.ImageField(upload_to='media/workorder/%Y/%m/%d/%H/%M/%S/')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleConditionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_number', models.CharField(max_length=25, verbose_name='VIN')),
                ('registration_number', models.CharField(max_length=25, verbose_name='Registration Number')),
                ('mileage', models.IntegerField(verbose_name='Mileage')),
                ('fuel_level', models.IntegerField(choices=[('OPTION_ZERO', 0), ('OPTION_ONE', 1), ('OPTION_TWO', 2), ('OPTION_THREE', 3), ('OPTION_FOUR', 4), ('OPTION_FIVE', 5), ('OPTION_SIX', 6), ('OPTION_SEVEN', 7), ('OPTION_EIGHT', 8), ('OPTION_NINE', 9), ('OPTION_TEN', 10)], default='OPTION_ZERO', verbose_name='Fuel Level')),
                ('main_keys', models.CharField(choices=[('OPTION_ZERO', 0), ('OPTION_ONE', 1), ('OPTION_TWO', 2)], default='OPTION_ZERO', max_length=15, verbose_name='Main Keys')),
                ('transponder_keys', models.CharField(choices=[('OPTION_ZERO', 0), ('OPTION_ONE', 1)], default='OPTION_ZERO', max_length=15, verbose_name='Transponder Keys')),
                ('registration_certificate', models.CharField(choices=[('OPTION_ZERO', 'No'), ('OPTION_ONE', 'Original'), ('OPTION_TWO', 'Photocopy')], default='OPTION_ZERO', max_length=15, verbose_name='Registration Certificate')),
                ('first_aid_kit', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='First Aid Kit')),
                ('high_visibility_waistcoat', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='High Visibility Waistcoat')),
                ('warning_triangle', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Warning Triangles')),
                ('luggage_net', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Luggage Net')),
                ('floor_mats', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Floor Mats')),
                ('rear_boot_rubber_mat', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Rear Boot Rubber Mat')),
                ('charging_cable_type2', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Charging Cable Type2')),
                ('charging_cable_schuko', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Charging Cable Schuko')),
                ('tyre_set', models.CharField(choices=[('OPTION_ZERO', 'Summer Tyre'), ('OPTION_ONE', 'Winter Tyre')], default='OPTION_ZERO', max_length=12, verbose_name='Tyre Set')),
                ('tow_bar', models.CharField(choices=[('OPTION_ZERO', False), ('OPTION_ONE', True)], default='OPTION_ZERO', max_length=15, verbose_name='Tow Bar')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('proof_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiclecondition.proofimagesmodel')),
            ],
        ),
    ]
