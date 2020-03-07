# Generated by Django 2.1.7 on 2019-08-03 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20190730_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='pythontraining.blr@gmail.com', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='project',
            field=models.CharField(choices=[('Flow Development', 'Flow Development'), ('Flow Tester', 'Flow Tester'), ('Project Tracker', 'Project Tracker'), ('Clearcase Developer', 'Clearcase Developer')], default='Clearcase Developer', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2019, 8, 3, 4, 34, 2, 368556)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doj',
            field=models.DateField(default=datetime.datetime(2019, 8, 3, 4, 34, 2, 368577)),
        ),
    ]
