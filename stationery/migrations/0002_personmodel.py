# Generated by Django 5.0.4 on 2024-04-05 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.addressmodel')),
            ],
        ),
    ]
