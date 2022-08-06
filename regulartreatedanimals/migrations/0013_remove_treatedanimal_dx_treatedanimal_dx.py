# Generated by Django 4.0 on 2022-06-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulartreatedanimals', '0012_disease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatedanimal',
            name='dx',
        ),
        migrations.AddField(
            model_name='treatedanimal',
            name='dx',
            field=models.ManyToManyField(blank=True, to='regulartreatedanimals.Disease', verbose_name='Dx'),
        ),
    ]