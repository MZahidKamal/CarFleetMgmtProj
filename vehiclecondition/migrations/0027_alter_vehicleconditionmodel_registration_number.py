# Generated by Django 5.0.4 on 2024-04-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0026_remove_cargivingvcmodel_wo_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleconditionmodel',
            name='registration_number',
            field=models.CharField(max_length=10, verbose_name='Registration Number'),
        ),
    ]
