# Generated by Django 2.1.7 on 2019-02-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190225_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catedra',
            name='catedra_days',
        ),
        migrations.AddField(
            model_name='catedra',
            name='catedra_dias',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
