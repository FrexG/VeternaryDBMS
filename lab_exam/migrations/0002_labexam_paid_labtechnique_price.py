# Generated by Django 4.0 on 2022-08-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labexam',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labtechnique',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
