# Generated by Django 2.1.7 on 2019-02-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_catedra_catedra_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catedra',
            name='catedra_dias',
        ),
        migrations.AddField(
            model_name='catedra',
            name='catedra_dia',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
