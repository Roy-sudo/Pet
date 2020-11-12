# Generated by Django 3.0.2 on 2020-05-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_booking_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('S', 'small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
