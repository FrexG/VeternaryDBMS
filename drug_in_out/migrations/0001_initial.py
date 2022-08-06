# Generated by Django 4.0 on 2022-07-10 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registernewuser', '0012_remove_customer_treatment_history'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Health Post', 'HP'), ('Zone Reverse', 'ZR'), ('Emergency', 'Emergency'), ('Expired Drugs', 'Expired'), ('General Sale', 'General')], max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('batch_number', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=200, null=True)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='approved_by', to='auth.user')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registernewuser.drug')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registernewuser.kebele')),
                ('store_man', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='store_man', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='DrugIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('Regular Fund', 'Regular'), ('Revolving Fund', 'Revolving'), ('Zone Support', 'Zone'), ('Regional Support', 'Regional'), ('Non-Govermental', 'NGO'), ('Other', 'Other')], max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('batch_number', models.CharField(max_length=100)),
                ('expiration_data', models.DateField()),
                ('remark', models.CharField(max_length=200, null=True)),
                ('dropped_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dropped_by', to='auth.user')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registernewuser.drug')),
                ('receiver', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to='auth.user')),
            ],
        ),
    ]