# Generated by Django 4.0 on 2022-07-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_in_out', '0002_clinicalequipmentcashdeposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalequipmentin',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='clinicalequipmentout',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
