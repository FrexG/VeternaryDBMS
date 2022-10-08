# Generated by Django 3.1.3 on 2021-03-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0005_auto_20210328_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
            ],
        ),
    ]
