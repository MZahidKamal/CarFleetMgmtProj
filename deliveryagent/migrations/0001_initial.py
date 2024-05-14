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
            name='DeliveryAgentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.personmodel', verbose_name='Personal Info')),
            ],
            options={
                'verbose_name': 'Delivery Agent',
                'verbose_name_plural': 'Delivery Agents',
            },
        ),
    ]
