# Generated by Django 3.1.3 on 2021-06-26 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0010_auto_20210624_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalservice',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinicalservices.service'),
            preserve_default=False,
        ),
    ]
