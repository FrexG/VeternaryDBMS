# Generated by Django 4.0 on 2022-07-14 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('drug_in_out', '0007_alter_drogoutcashdeposit_confirmed_by'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DrogOutCashDeposit',
            new_name='DrugOutCashDeposit',
        ),
    ]
