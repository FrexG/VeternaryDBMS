# Generated by Django 4.0 on 2022-07-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Adminstrator'), ('Cashier', 'Cashier'), ('Vet', 'Veternarian'), ('Pharmacist', 'Pharmacist'), ('Stock_Keeper', 'Stock Keeper')], max_length=100),
        ),
    ]