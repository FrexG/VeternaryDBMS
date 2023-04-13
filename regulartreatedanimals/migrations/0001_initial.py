# Generated by Django 3.1.3 on 2021-03-29 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registernewuser', '0006_drug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.TextField(max_length=50, verbose_name='Unit Name')),
            ],
        ),
        migrations.CreateModel(
            name='TreatedAnimals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t0', models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='T0')),
                ('pr', models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='PR')),
                ('rr', models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='RR')),
                ('clinical_finding', models.TextField(blank=True, max_length=200, verbose_name='Clinical Finding')),
                ('dx', models.TextField(max_length=100, verbose_name='DX')),
                ('differential_diag', models.TextField(max_length=100, verbose_name='Differential Diagnosis')),
                ('rumen_motility', models.TextField(max_length=100, verbose_name='Rumen Motility')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('service_date', models.DateField(auto_now_add=True, verbose_name='Service Date')),
                ('case_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.customer', verbose_name='Case Number')),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.drug', verbose_name='RX')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regulartreatedanimals.unit', verbose_name='Unit')),
            ],
        ),
    ]
