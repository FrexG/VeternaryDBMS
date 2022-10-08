# Generated by Django 4.0 on 2022-08-02 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registernewuser', '0012_remove_customer_treatment_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_sample', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LabTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_technique', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_result', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.customer')),
                ('lab_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_exam.labsample')),
                ('lab_technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_exam.labtechnique')),
            ],
        ),
    ]
