# Generated by Django 4.0 on 2022-08-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0014_alter_drug_dis_price_alter_drug_stock_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='dis_unit',
            field=models.CharField(default='ML', max_length=50),
        ),
        migrations.AddField(
            model_name='drug',
            name='stokc_unit',
            field=models.CharField(default='BOX', max_length=50),
        ),
    ]
