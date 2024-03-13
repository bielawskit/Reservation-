# Generated by Django 3.2.16 on 2023-02-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                ("location", models.CharField(max_length=35)),
                ("quantity", models.IntegerField()),
                (
                    "multisport",
                    models.IntegerField(
                        choices=[(1, "Akceptuje"), (2, "Nie akceptuje")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                ("surname", models.CharField(max_length=35)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Court",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "type",
                    models.IntegerField(
                        choices=[(1, "Sztuczna trawa"), (2, "Mączka"), (3, "Beton")]
                    ),
                ),
                (
                    "preference",
                    models.IntegerField(choices=[(1, "wewnętrzny"), (2, "zewnętrzny")]),
                ),
                ("cost", models.IntegerField()),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="club.club"
                    ),
                ),
            ],
        ),
    ]
