# Generated by Django 4.0 on 2022-08-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0018_remove_customer_breed_remove_customer_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
