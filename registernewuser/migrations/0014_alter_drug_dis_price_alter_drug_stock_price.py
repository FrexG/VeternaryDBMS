# Generated by Django 4.0 on 2022-08-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0013_rename_price_drug_dis_price_drug_stock_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='dis_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='drug',
            name='stock_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
