# Generated by Django 3.1.3 on 2021-03-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0002_auto_20210328_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
    ]
