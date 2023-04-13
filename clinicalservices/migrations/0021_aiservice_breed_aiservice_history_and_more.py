# Generated by Django 4.0 on 2022-08-12 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registernewuser', '0019_alter_customer_mobile_number'),
        ('clinicalservices', '0020_rename_quantity_aiservice_qnty'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiservice',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registernewuser.breed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aiservice',
            name='history',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aiservice',
            name='number_of_animals',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aiservice',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aiservice',
            name='species',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registernewuser.species'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registernewuser.breed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='history',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='number_of_animals',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicalservice',
            name='species',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registernewuser.species'),
            preserve_default=False,
        ),
    ]