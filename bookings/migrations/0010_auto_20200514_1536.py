# Generated by Django 3.0.2 on 2020-05-14 12:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_booking_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
