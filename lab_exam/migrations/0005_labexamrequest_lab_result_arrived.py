# Generated by Django 4.0 on 2022-08-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_exam', '0004_labexamrequest_labresult_delete_labexam'),
    ]

    operations = [
        migrations.AddField(
            model_name='labexamrequest',
            name='lab_result_arrived',
            field=models.BooleanField(default=False),
        ),
    ]
