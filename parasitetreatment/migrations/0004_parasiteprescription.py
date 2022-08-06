# Generated by Django 4.0 on 2022-06-21 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regulartreatedanimals', '0008_prescription_paid'),
        ('registernewuser', '0010_alter_drug_price'),
        ('parasitetreatment', '0003_remove_parasitetreatment_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParasitePrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('duration', models.PositiveIntegerField(verbose_name='Follow Up Duration')),
                ('paid', models.BooleanField(default=False)),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.drug', verbose_name='RX')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parasitetreatment.parasitetreatment', verbose_name='Treatment ID')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regulartreatedanimals.unit', verbose_name='Unit')),
            ],
        ),
    ]