# Generated by Django 3.2.6 on 2021-08-22 16:29

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MovieCast",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("actor_name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=128)),
                ("imdbid", models.CharField(max_length=10)),
                ("year", models.CharField(max_length=15)),
                ("data", models.JSONField(blank=True, default=dict)),
                ("poster", models.URLField(blank=True)),
                ("type", models.CharField(default="movie", max_length=10)),
                ("cast", models.ManyToManyField(blank=True, related_name="movies", to="api.MovieCast")),
            ],
            options={
                "ordering": ["-year", "title"],
            },
            managers=[
                ("omdb", django.db.models.manager.Manager()),
            ],
        ),
    ]
