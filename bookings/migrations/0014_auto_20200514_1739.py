# Generated by Django 3.0.2 on 2020-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_auto_20200514_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('Grooming', (('Dogs Full Bath', 'Dogs'), ('Dogs Bath and Haircut', 'DogsB'), ('Cats Full Package', 'Cats'), ('Dogs Full Bath', 'Dogs'), ('Pick 3 Spa', 'Spa'), ('Deshedding Service', 'Deshedding'), ('Deshedding Deluxe Package', 'Deluxe'))), ('Pet Boarding', (('boarding', 'Boarding'), ('house sitting', 'sitting'), ('pet walking', 'Pet Walking'), ('pet daycare', 'Pet Daycare'), ('drop-in-visit', 'Drop-In-Visit'))), ('Rent_cage', (('cat', 'Cat'), ('dog', 'Dog')))], max_length=30),
        ),
    ]
