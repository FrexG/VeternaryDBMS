# Generated by Django 4.0 on 2022-08-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_in_out', '0005_remove_clinicalequipmentin_expiration_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicalequipmentout',
            old_name='receiver',
            new_name='kebele',
        ),
        migrations.AddField(
            model_name='clinicalequipmentout',
            name='received_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
