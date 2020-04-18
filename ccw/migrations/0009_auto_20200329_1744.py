# Generated by Django 2.2.11 on 2020-03-29 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ccw', '0008_ccworderdetails_requestedstartdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ccworderdetails',
            name='RSD',
        ),
        migrations.AlterField(
            model_name='ccworderdetails',
            name='requestedStartDate',
            field=models.DateField(default=datetime.datetime(2020, 3, 29, 12, 14, 16, 236517, tzinfo=utc)),
        ),
    ]