# Generated by Django 4.0 on 2022-07-10 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drug_in_out', '0002_alter_drugin_source_alter_drugout_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugin',
            name='date_received',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
