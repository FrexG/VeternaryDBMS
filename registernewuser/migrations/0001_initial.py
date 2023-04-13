# Generated by Django 3.1.3 on 2021-03-28 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kebele',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=100)),
                ('sub_kebele', models.CharField(max_length=100)),
                ('case_number', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_animals', models.IntegerField()),
                ('sex', models.CharField(max_length=2)),
                ('service_date', models.DateField(auto_now_add=True)),
                ('treatment_history', models.CharField(max_length=250, null=True)),
                ('mobile_number', models.IntegerField()),
                ('breed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.breed')),
                ('kebele_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.kebele')),
                ('species_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.species')),
            ],
        ),
    ]
