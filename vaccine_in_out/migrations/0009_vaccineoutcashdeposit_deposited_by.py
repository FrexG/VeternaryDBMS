# Generated by Django 4.2.2 on 2023-07-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_in_out', '0008_remove_vaccineoutcashdeposit_payment_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccineoutcashdeposit',
            name='deposited_by',
            field=models.CharField(default='NOT PROVIDED', max_length=100),
        ),
    ]
