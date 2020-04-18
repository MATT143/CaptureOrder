# Generated by Django 2.2.11 on 2020-03-28 10:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ccw', '0006_auto_20200328_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerSetupDetails',
            fields=[
                ('offerId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('offer', models.CharField(max_length=20)),
                ('deliveryMethod', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='offerSetup',
        ),
    ]
