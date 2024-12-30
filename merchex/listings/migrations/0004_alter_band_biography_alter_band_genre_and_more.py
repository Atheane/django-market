# Generated by Django 4.2.17 on 2024-12-30 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0003_band_active_band_biography_band_genre_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="biography",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AlterField(
            model_name="band",
            name="genre",
            field=models.CharField(
                default="HH",
                max_length=5,
                verbose_name=[
                    ("HH", "Hip Hop"),
                    ("SP", "Synth Pop"),
                    ("AR", "Alternative Rock"),
                    ("E", "Electronic"),
                    ("H", "House"),
                    ("DH", "Deep House"),
                    ("MT", "Minimal Tech"),
                    ("T", "Techno"),
                    ("C", "Classic"),
                    ("PE", "Progressive Electronic"),
                    ("IR", "Indie Rock"),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="band",
            name="year_formed",
            field=models.IntegerField(
                default=2000,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2021),
                ],
            ),
        ),
    ]
