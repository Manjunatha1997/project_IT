# Generated by Django 3.0.3 on 2020-02-21 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20200208_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 2, 21, 19, 57, 36, 313386)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doj',
            field=models.DateField(default=datetime.datetime(2020, 2, 21, 19, 57, 36, 313386)),
        ),
    ]