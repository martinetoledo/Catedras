# Generated by Django 2.1.7 on 2019-02-26 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190225_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catedra',
            old_name='catedra_dia',
            new_name='catedra_days',
        ),
    ]
