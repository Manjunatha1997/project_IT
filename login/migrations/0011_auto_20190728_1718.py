# Generated by Django 2.1.7 on 2019-07-28 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20190728_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 7, 28, 17, 18, 9, 408905)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doj',
            field=models.DateField(default=datetime.datetime(2019, 7, 28, 17, 18, 9, 408943)),
        ),
    ]
