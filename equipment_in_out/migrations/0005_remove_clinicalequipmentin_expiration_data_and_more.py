# Generated by Django 4.0 on 2022-08-03 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_in_out', '0004_clinicalequipmentout_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicalequipmentin',
            name='expiration_data',
        ),
        migrations.RemoveField(
            model_name='clinicalequipmentin',
            name='total',
        ),
        migrations.RemoveField(
            model_name='clinicalequipmentin',
            name='unit_price',
        ),
        migrations.RemoveField(
            model_name='clinicalequipmentout',
            name='total',
        ),
        migrations.RemoveField(
            model_name='clinicalequipmentout',
            name='unit_price',
        ),
        migrations.DeleteModel(
            name='ClinicalEquipmentCashDeposit',
        ),
    ]
