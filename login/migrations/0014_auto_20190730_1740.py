# Generated by Django 2.1.7 on 2019-07-30 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20190728_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 7, 30, 17, 40, 37, 535217)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doj',
            field=models.DateField(default=datetime.datetime(2019, 7, 30, 17, 40, 37, 535250)),
        ),
    ]