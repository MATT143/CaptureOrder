# Generated by Django 2.2.11 on 2020-03-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccw', '0005_auto_20200328_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offersetup',
            name='offer',
            field=models.CharField(max_length=20),
        ),
    ]