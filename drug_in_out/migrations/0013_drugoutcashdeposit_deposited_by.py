# Generated by Django 4.2.2 on 2023-07-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug_in_out', '0012_remove_drugoutcashdeposit_payment_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugoutcashdeposit',
            name='deposited_by',
            field=models.CharField(default='Not Given', max_length=100),
        ),
    ]
