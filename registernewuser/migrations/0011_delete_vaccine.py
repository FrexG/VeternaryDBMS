# Generated by Django 4.0 on 2022-07-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parasitetreatment', '0009_delete_vaccination'),
        ('registernewuser', '0010_alter_drug_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vaccine',
        ),
    ]