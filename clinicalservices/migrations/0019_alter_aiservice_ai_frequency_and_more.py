# Generated by Django 4.0 on 2022-06-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0018_remove_aiservice_service_type_aiservice_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiservice',
            name='ai_frequency',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='bull_number',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='pd_result',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
