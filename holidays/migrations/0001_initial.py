# Generated by Django 2.1.7 on 2019-07-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
