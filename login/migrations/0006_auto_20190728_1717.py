# Generated by Django 2.1.7 on 2019-07-28 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190728_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 7, 28, 17, 16, 57, 859114)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doj',
            field=models.DateField(default=datetime.datetime(2019, 7, 28, 17, 16, 57, 859136)),
        ),
    ]