# Generated by Django 4.0 on 2022-07-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug_in_out', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugin',
            name='source',
            field=models.CharField(choices=[('Regular', 'Regular Fund'), ('Revolving', 'Revolving Fund'), ('Zone', 'Zone Support'), ('Regional', 'Regional Support'), ('NGO', 'Non-Govermental'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drugout',
            name='destination',
            field=models.CharField(choices=[('HP', 'Health Post'), ('ZR', 'Zone Reverse'), ('Emergency', 'Emergency'), ('Expired', 'Expired Drugs'), ('General', 'General Sale')], max_length=50),
        ),
    ]
