# Generated by Django 3.0.2 on 2020-03-24 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200321_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 33, 17, 754586)),
        ),
        migrations.AddField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 3, 24, 15, 33, 40, 433969, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
