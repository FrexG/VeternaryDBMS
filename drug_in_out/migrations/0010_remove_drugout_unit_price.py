# Generated by Django 4.0 on 2022-08-03 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drug_in_out', '0009_rename_date_received_drugin_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugout',
            name='unit_price',
        ),
    ]