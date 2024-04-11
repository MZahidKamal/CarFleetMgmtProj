# Generated by Django 5.0.4 on 2024-04-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0006_alter_companymodel_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='registration_number',
            field=models.CharField(max_length=100, unique=True, verbose_name='Registration Number'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='email_address',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='phone_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Phone Number'),
        ),
    ]
