# Generated by Django 4.0 on 2022-06-18 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0014_auto_20210706_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicalservice',
            name='service',
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='service_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='clinicalservices.service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clinicalservice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
