# Generated by Django 3.2.16 on 2024-03-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="location",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="club",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
