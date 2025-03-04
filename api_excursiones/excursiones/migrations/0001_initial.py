# Generated by Django 3.0.6 on 2020-06-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_excursion', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('disponibilidad', models.IntegerField()),
                ('precio', models.FloatField()),
            ],
        ),
    ]
