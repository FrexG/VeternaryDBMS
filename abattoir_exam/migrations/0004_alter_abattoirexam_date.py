# Generated by Django 4.0 on 2022-08-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abattoir_exam', '0003_alter_abattoirexam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abattoirexam',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]