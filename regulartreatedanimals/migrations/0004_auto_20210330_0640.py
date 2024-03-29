# Generated by Django 3.1.3 on 2021-03-30 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0007_auto_20210330_0640'),
        ('regulartreatedanimals', '0003_auto_20210329_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatedanimal',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='treatedanimal',
            name='rx',
        ),
        migrations.RemoveField(
            model_name='treatedanimal',
            name='unit',
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('duration', models.PositiveIntegerField(verbose_name='Follow Up Duration')),
                ('rx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registernewuser.drug', verbose_name='RX')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regulartreatedanimals.treatedanimal', verbose_name='Treatment')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regulartreatedanimals.unit', verbose_name='Unit')),
            ],
        ),
    ]
