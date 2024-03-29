# Generated by Django 3.2.16 on 2024-03-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_nip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=60, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(max_length=25, verbose_name="Imię"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="surname",
            field=models.CharField(max_length=30, verbose_name="Nazwisko"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="telephone_number",
            field=models.CharField(max_length=12, verbose_name="Numer telefonu"),
        ),
    ]
