# Generated by Django 5.0.4 on 2024-04-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0005_alter_companymodel_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='employees',
            field=models.ManyToManyField(blank=True, to='stationery.employeemodel', verbose_name='Employees'),
        ),
    ]