# Generated by Django 3.1.3 on 2021-03-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulartreatedanimals', '0004_auto_20210330_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
    ]
