# Generated by Django 3.1.3 on 2021-04-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalservices', '0002_auto_20210408_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalservices.service', verbose_name='Service Type'),
        ),
        migrations.AlterField(
            model_name='serviceprovided',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalservices.service', verbose_name='Service Type'),
        ),
    ]