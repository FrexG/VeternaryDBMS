# Generated by Django 4.0 on 2022-08-03 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0004_remove_vaccination_unit'),
        ('parasitetreatment', '0012_remove_parasiteprescription_unit'),
        ('stock', '0004_alter_clinicalequipment_unit'),
        ('regulartreatedanimals', '0016_alter_prescription_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='unit',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
