# Generated by Django 2.1.7 on 2019-02-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catedra_nombre', models.CharField(max_length=250)),
                ('catedra_comision', models.IntegerField()),
                ('catedra_depto', models.CharField(max_length=250)),
                ('catedra_materia', models.CharField(max_length=250)),
                ('catedra_horario', models.CharField(max_length=250)),
            ],
        ),
    ]
