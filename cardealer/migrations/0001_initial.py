# Generated by Django 5.0.4 on 2024-05-13 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stationery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDealerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.companymodel', verbose_name='Company Info')),
            ],
            options={
                'verbose_name': 'Car Dealer',
                'verbose_name_plural': 'Car Dealers',
            },
        ),
    ]
