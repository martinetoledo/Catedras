# Generated by Django 2.1.7 on 2019-02-26 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedra',
            name='catedra_depto',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]