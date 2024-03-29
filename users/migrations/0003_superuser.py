# Generated by Django 3.2.16 on 2023-02-10 12:44
import os

from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(apps, schema_editor):
    # CustomUser = apps.get_model('users', 'CustomUser')
    CustomUser = get_user_model()

    DJ_SU_EMAIL = os.environ.get("DJ_SU_EMAIL")
    DJ_SU_NAME = os.environ.get("DJ_SU_NAME")
    DJ_SU_SURNAME = os.environ.get("DJ_SU_SURNAME")
    DJ_SU_PASSWORD = os.environ.get("DJ_SU_PASSWORD")

    CustomUser.objects.create_superuser(
        email=DJ_SU_EMAIL,
        name=DJ_SU_NAME,
        surname=DJ_SU_SURNAME,
        password=DJ_SU_PASSWORD,
    )


def delete_superuser(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_groups"),
    ]

    operations = [migrations.RunPython(create_superuser, delete_superuser)]
