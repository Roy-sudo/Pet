# Generated by Django 3.0.2 on 2020-05-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0018_auto_20200514_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='forename',
            field=models.CharField(max_length=20, verbose_name='Owner name'),
        ),
    ]