# Generated by Django 4.0 on 2022-06-20 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0015_remove_clinicalservice_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalservice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
