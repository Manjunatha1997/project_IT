# Generated by Django 2.1.7 on 2019-07-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0004_auto_20190728_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheetdata',
            name='approver',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
