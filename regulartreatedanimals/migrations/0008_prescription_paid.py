# Generated by Django 4.0 on 2022-06-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulartreatedanimals', '0007_alter_unit_unit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]