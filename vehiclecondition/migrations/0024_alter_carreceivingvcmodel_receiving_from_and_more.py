# Generated by Django 5.0.4 on 2024-04-12 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclecondition', '0023_remove_cardeliveringvcmodel_signature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreceivingvcmodel',
            name='receiving_from',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Receiving From'),
        ),
        migrations.CreateModel(
            name='CarGivingVCModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wo_number', models.CharField(max_length=25, verbose_name='WO')),
                ('giving_to', models.CharField(blank=True, max_length=50, null=True, verbose_name='Giving To')),
                ('created_on', models.DateField(auto_now_add=True, null=True, verbose_name='Date and Time')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Location')),
                ('e_signature', models.ImageField(blank=True, null=True, upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='E-Signature')),
                ('vehicle_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehiclecondition.vehicleconditionmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='CarDeliveringVCModel',
        ),
    ]