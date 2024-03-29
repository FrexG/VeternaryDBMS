# Generated by Django 4.0 on 2022-08-02 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registernewuser', '0012_remove_customer_treatment_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_code', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AbattoirExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('body_weight', models.PositiveIntegerField()),
                ('t0', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='T0')),
                ('pr', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PR')),
                ('rr', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='RR')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('result', models.CharField(choices=[('R', 'Rejected'), ('C', 'Confirmed')], max_length=100)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='abattoir_exam.color')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abattoir_exam.hotel')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='abattoir_exam.origin')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registernewuser.species')),
            ],
        ),
    ]
