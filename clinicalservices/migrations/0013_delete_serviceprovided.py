# Generated by Django 3.1.3 on 2021-07-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0012_auto_20210626_1207'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceProvided',
        ),
    ]